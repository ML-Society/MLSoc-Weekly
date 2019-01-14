# Provides helper for loading the data to np
# array

import numpy as np
import os

from urllib.request import urlopen
from sklearn.model_selection import train_test_split

data_uri = "https://raw.githubusercontent.com/jadeyee/r2d3-part-1-data/master/part_1_data.csv"

def _load_data():
    """
    Returns data in np array sorted as:
    in_sf,beds,bath,price,year_built,sqft,price_per_sqft,elevation
    """
    res = ""
    if os.path.isfile("./.data"):
        with open("./.data", "r") as f:
            res = f.read()
    else:
        u = urlopen(data_uri)
        res = u.read().decode(u.headers.get_content_charset())
        # Make local backup
        with open("./.data", "w") as f:
            f.write(res)
    return np.loadtxt("./.data", delimiter=",", comments="#", skiprows=3, unpack=True)
    

def load_train_data():
    """
    Returns X_train, y_train with 8:2 split and random_state=0
    """
    s_sf, beds, bath, price, year_built, sqft, price_per_sqft, elevation = _load_data()
    
    X = np.column_stack((beds, bath, price, year_built, sqft, price_per_sqft, elevation))
    y = s_sf

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=0)
    return X_train, y_train

def _load_test_data():
    """
    Returns X_test, y_test with 8:2 split and random_state=0
    """
    s_sf, beds, bath, price, year_built, sqft, price_per_sqft, elevation = _load_data()
    
    X = np.column_stack((beds, bath, price, year_built, sqft, price_per_sqft, elevation))
    y = s_sf

    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    return X_test, y_test

def grade(fn):
    """
    Grade a function, which classifies the data. The function is
    passed:
    np.column_stack((beds,bath,price,year_built,sqft,price_per_sqft,elevation))
    """
    X, y = _load_test_data()
    
    pred = fn(X)
    target = y

    return 1 - (np.sum(np.abs(pred-target)) / len(target))
