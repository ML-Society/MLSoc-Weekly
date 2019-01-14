from sklearn import tree
from sklearn import svm
import numpy as np

import data

def ex1_fn(X_train, y_train, random_state=0):
    params = {
        # add params here
        'random_state': random_state,
    }
    # decision tree ~1 line (NOTE: only pass params as **params e.g. DecisionTree(**params))
    # fit tree ~1 line
    # print("Grade: ", data.grade(pred_fn)) # pred_fn => classfier_obj.predict (extract reference from object!)

    return # pred_fn


def ex2_fn(X_train, y_train, random_state=0):
    params = {
        # add params here
        'random_state': random_state,
    }
    # svm LINEAR classifier ~1 line # (NOTE: only pass params as **params)
    # fit classifier
    # print("Grade: ", data.grade(pred_fn))

    # return pred_fn

## test [0.1, 1.0, 10] ## choose best param from these
def ex3_fn(X_train, y_train, random_state=0):
    params = {
        # add params here
        'random_state': random_state,
        #'C': ???,
    }
    # svc classifier, default kernel aka 'rbf' ~1 line
    # fit classifier ~1 line
    # print("Grade: ", data.grade(pred_fn))

    # return pred_fn


if __name__ == "__main__":
    X_train, y_train = data.load_train_data()
    ex1_fn(X_train, y_train)
    ex2_fn(X_train, y_train)
    ex3_fn(X_train, y_train)



### Expected results
### all these are from using random_state=0
### EX1_MIN_ACC, EX2_MIN_ACC, EX3_MIN_ACC = 0.85, 0.42, 0.69