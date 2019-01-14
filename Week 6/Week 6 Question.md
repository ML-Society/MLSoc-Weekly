# Question

Train a decision tree, that trains on the data given back from `load_test_data()`.

    # Returns data in np array sorted as:
    in_sf,beds,bath,price,year_built,sqft,price_per_sqft,elevation = load_data()

Then, write a function that uses this decision tree. Try to get at least 70% on
`grade()`. Your function is given the following arguments as arrays, and is expected to
return a numpy array that labels if the entry at the ith index is in San-Francisco, using
`1` or `0`.

    # Arguments
    beds,bath,price,year_built,sqft,price_per_sqft,elevation

Both these functions are available in `data.py` (`import data`).
