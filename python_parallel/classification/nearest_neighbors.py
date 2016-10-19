"""
Naive, inefficient Python implementation of the nearest 
neighbor classification algorithm.
"""
import numpy as np

def nearest_neighbor_prediction( X_test, X_train, y_train ):
    """
    Given a set of training examples X_train (with corresponding
    labels y_train), predict the labels that correspond to the test 
    examples X_test. 

    The prediction is done by finding the nearest training example,
    and predicting the same label. 

    Parameters
    ----------
    X_test: 2darray of shape (n_test, n_features)
    X_train: 2darray of shape (n_train, n_features)
    y_train: 1darray of shape (n_train,)

    Returns
    -------
    y_testL 1darray of shape (n_test,)
    """
    n_test = len(X_test)
    y_test = np.zeros(n_test)

    # Go through each test sample
    for i_test in range( n_test ):

        # Calculate the distance between this sample
        # and each training example
        this_test = X_test[i_test]
        distance = np.sum( (this_test[np.newaxis,:] - X_train)**2, axis=1)

        # Find the index of the nearest training example
        i_nearest_train = np.argmin( distance )

        # Register the corresponding label
        y_test[i_test] = y_train[i_nearest_train]

    return( y_test )

        
        
    
