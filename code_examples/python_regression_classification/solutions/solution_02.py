from sklearn.neural_network import MLPClassifier

# Initialize ANN classifier

# create an ANN with two hidden layers, each with 10 neurons
hidden_layer_sizes = (10, 10)

# using a logistic activation function
activation = 'logistic'

mlp = MLPClassifier(hidden_layer_sizes= hidden_layer_sizes, activation=activation, \
                    max_iter = 2000, random_state=13)
                    
# Train the classifier with the traning data
mlp.fit(X,y)

# predict results from the test data
predicted = mlp.predict(X)

# plot the confusion matrix
cm = confusion_matrix(y,predicted)
plot_confusion_matrix(cm, classes=iris.target_names,
                      title='Confusion matrix, without normalization')