"""
This script was used to create the examples datasets 
train_images.npy, train_labels.npy, test_images.npy
"""
import numpy as np
from sklearn.datasets import fetch_mldata

# Download the MNIST dataset
mnist = fetch_mldata('MNIST original')

# Shuffle it
target = mnist.target.reshape(len(mnist.target),1)
X = np.hstack( (mnist.data, target))
np.random.shuffle( X )
images = X[:, :-1]
labels = X[:, -1]

# Split into training and testing data
N_train = 2000
N_test = 1000
train_images = images[:N_train]
train_labels = labels[:N_train]
test_images = images[N_train:N_train+N_test]
test_labels = labels[N_train:N_train+N_test]

# Save the data
np.save('train_images.npy', train_images)
np.save('train_labels.npy', train_labels)
np.save('test_images.npy', test_images)
