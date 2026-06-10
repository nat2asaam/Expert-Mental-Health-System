import numpy as np
import matplotlib.pyplot as plt
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def sigmoid_derivative(z):
    return sigmoid(z) * (1 - sigmoid(z))
def relu(z):
    return np.maximum(0, z)
def relu_derivative(z):
    return np.where(z > 0, 1, 0)
def tanh(z):
    return np.tanh(z)
def tanh_derivative(z):
    return 1 - np.tanh(z) ** 2
def graph_error(error_list):
    # Plot error
    plt.plot(error_list)
    plt.title('Error')
    plt.xlabel('Epochs')
    plt.ylabel('Error')
    plt.show()
def graph_activation_and_derivative(z,activation1,derivative1,label11,label12,title1,activation2,derivative2,label21,label22,title2):
    plt.figure(figsize=(12, 6))
    #plot for activatio1 and its derivative
    plt.subplot(1, 2, 1)
    plt.plot(z, activation1, label=label11,color='b')
    plt.plot(z, derivative1, label=label12,color='r',linestyle='--')
    plt.title(title1)
    plt.xlabel('Input Value (z)')
    plt.ylabel('Activation / Gradient')
    plt.legend()
    #plot activation2 and its derivative
    plt.subplot(1, 2, 2)
    plt.plot(z, activation2, label=label21, color='g')
    plt.plot(z, derivative2, label=label22, color='r',linestyle='--')
    plt.title(title2) 
    plt.xlabel('Input Value (z)')
    plt.ylabel('Activation / Gradient')
    plt.legend()

    plt.tight_layout()
    plt.show()
