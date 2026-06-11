# This script is for medical diagnosis of bi-polar disorder with the symptoms below which are commonly associated with manic episodes in bipolar disorder:
# The symptoms are the features or inputs to the neural network and the output is the likelihood of having bipolar disorder based on these symptoms.
# Below are the 7 symptoms:
# Feeling overly happy or high
# Having a decreased need for sleep
# Talking fast
# Feeling extremely restless or impulsive
# Being easily distracted
# Having over confidence in your abilities
# Engaging in risky activities
import numpy as np
from BiPolar import activation_utility as act
import pickle
def initialize_network_parameters():
    inputSize=7 # number of input neurons
    hiddenSize=3 # number of hidden neurons
    outputSize=1 # number of output neurons  
    lr=0.01 # learning rate
    epochs=1000000 # number of epochs
    w1=np.random.rand(hiddenSize,inputSize) * 2-1 # weights for input to hidden layer
    b1=np.random.rand(hiddenSize,1) * 2-1 # bias for hidden layer
    w2=np.random.rand(outputSize,hiddenSize) * 2-1 # weights for hidden to output layer
    b2=np.random.rand(outputSize,1) * 2-1 # bias for output layer
    return w1,b1,w2,b2,lr,epochs
def train_model():
    # Generate the input dataset
    X=np.indices((2,)*7).reshape(7,-1).T
    X=X.astype(np.float32)
    # Generate the target dataset
    d=np.mean(X, axis=1)
    d=d.reshape(1,-1)
    w1,b1,w2,b2,lr,epochs=initialize_network_parameters()
    error_list = []
    # train the network
    for epoch in range(epochs):
        # forward pass
        z1=np.dot(w1,X.T)+b1 # weighted sum for hidden layer
        # a1=1.0/(1.0+np.exp(-z1)) # sigmoid activation for hidden layer
        a1 = act.relu(z1)  # ReLU activation for hidden layer
        z2=np.dot(w2,a1)+b2 # weighted sum for output layer
        # a2=1.0/(1.0+np.exp(-z2)) # sigmoid activation for output layer
        a2=act.sigmoid(z2)
        # compute error
        error=d-a2
        # backpropagation
        # dz2=error*a2*(1-a2) # derivative of output layer (sigmoid)
        dz2=error * act.sigmoid_derivative(z2) # derivative of output layer (sigmoid)
        da1=np.dot(w2.T,dz2)
        # dz1=da1* (a1*(1-a1)) # derivative of sigmoid for hidden layer
        dz1=da1 * act.relu_derivative(z1)  # derivative of sigmoid for hidden layer
        # update weights and biases
        w2+=lr*np.dot(dz2,a1.T) # update weights for hidden to output layer
        b2+=lr*np.sum(dz2,axis=1,keepdims=True)# update bias for output layer
        w1+=lr*np.dot(dz1,X) # update weights for input to hidden layer
        b1+=lr*np.sum(dz1,axis=1,keepdims=True) # update bias for hidden layer
        if (epoch + 1) % 10000 == 0:
            print("Epoch: %d, Average Error: %0.05f" % (epoch + 1, np.average(np.abs(error))))
            error_list.append(np.average(abs(error)))
            if (epoch+1)==1000000:
                # Plot ReLU and sigmoid activation functions and their derivatives
                act.graph_activation_and_derivative(z1,act.relu(z1),act.relu_derivative(z1),"ReLU Activation","ReLU Derivative","ReLU Activation and Derrivative",act.sigmoid(z1),act.sigmoid_derivative(z1),"Sigmoid Activation","Sigmoid Derivative","Sigmoid Activation and Derivative")
    # Testing the trained network
    z1 = np.dot(w1, X.T) + b1  # Weighted sum for hidden layer
    # a1 = 1 / (1 + np.exp(-z1))  # Sigmoid activation for hidden layer
    a1 = act.relu(z1)  # relu activation for hidden layer

    z2 = np.dot(w2, a1) + b2  # Weighted sum for output layer
    # a2 = 1 / (1 + np.exp(-z2))  # Sigmoid activation for output layer
    a2=act.sigmoid(z2) # Sigmoid activation for output layer
    # Print results
    print('Final output after training:', a2)
    print('Ground truth', d)
    print('Error after training:', error)
    print('Average error: %0.05f'%np.average(abs(error)))
    # Plot error
    act.graph_error(error_list)
    # return weights and biases
    my_model=w1,b1,w2,b2
    #save model parameters to a file
    with open("bipolar_model.pkl", "wb") as file:
        pickle.dump(my_model, file)
def load_model():
    with open("bipolar_model.pkl", "rb") as file:
        w1, b1, w2, b2 = pickle.load(file)
    return w1, b1, w2, b2
def predict(symptoms):
    w1, b1, w2, b2 = load_model()
    z1 = np.dot(w1, symptoms) + b1  # Weighted sum for hidden layer
    a1 = act.relu(z1)  # ReLU activation for hidden layer
    z2 = np.dot(w2, a1) + b2  # Weighted sum for output layer
    a2 = act.sigmoid(z2)  # Sigmoid activation for output layer
    return a2