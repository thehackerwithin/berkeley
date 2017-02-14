"""
This script was used to create the datasets
in the folders `setosa`, `versicolor`, `versicolor_4_features`
"""
import os
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the data and split into training and testing set
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = \
    train_test_split( iris['data'], iris['target'], test_size=0.2 )

# Define function to save the datasets
def save_from_pandas( X, y, label='train' ):
    df = pd.DataFrame( X, columns=iris['feature_names'] )
    df['species'] = y
    df['setosa'] = (df['species'] == 0).values.astype(np.float)
    df['versicolor'] = (df['species'] == 1).values.astype(np.float)

    # Dataset setosa
    if not os.path.exists('setosa'):
        os.mkdir('setosa')
    filename = os.path.join('setosa', label+'.csv')
    df[['petal length (cm)', 'petal width (cm)', 'setosa']].to_csv(filename, index=False)

    # Dataset versicolor
    if not os.path.exists('versicolor'):
        os.mkdir('versicolor')
    filename = os.path.join('versicolor', label+'.csv')
    df[['petal length (cm)', 'petal width (cm)', 'versicolor']].to_csv(filename, index=False)

    # Dataset versicolor 4 features
    if not os.path.exists('versicolor_4_features'):
        os.mkdir('versicolor_4_features')
    filename = os.path.join('versicolor_4_features', label+'.csv')
    df[ iris['feature_names'] + ['versicolor']].to_csv(filename, index=False)

# Save the datasets
save_from_pandas( X_train, y_train, 'train')
save_from_pandas( X_test, y_test, 'test')
