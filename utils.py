import numpy as np

def perceptron(weights, bias, inputs):
    ''' Perceptron fcn '''

    if len(weights)!=len(inputs):
        return print("Weights and inputs don't match in size!!!")
    
    y = 0
    for i in range(len(weights)):
        y += weights[i] * inputs[i]
        
    # Y = SUM(w_i*z_i) + bias
    return activate_fcn(y + bias)

def activate_fcn(input):
    ''' Activation fcn'''

    return heaviside(input)

def heaviside(input):
    ''' Activation fcn - heaviside'''

    return np.where(input >= 0, 1, 0)

def train(data, epoch = 1, learning_rate = 0.2):

    # init weights = 1, bias = 0
    weights = [1] * len(data[0][0])
    bias = 0

    for _ in range(epoch):
        for inputs, desired in data:
            y = perceptron(weights, bias, inputs)
            err = desired - y

            for i in range(len(weights)):
                weights[i] += err * inputs[i] * learning_rate

            bias += err * learning_rate

    return weights, bias

def loss_fcn(weights, bias, data):
    e = 0
    for inputs, desired in data:
        y = perceptron(weights, bias, inputs)
        e += (y - desired)**2

    return e/2