import numpy as np
import utils
from utils import perceptron, train
import pylab as plt
import torch

# DATASET
train_set = [
    #[(A,B), Y]
    [(0, 0), 0],
    [(0, 1), 0],
    [(1, 0), 0],
    [(1, 1), 1]
]

val_set = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1)
]

test_set = [
    [(0, 0), 0],
    [(0, 1), 0],
    [(1, 0), 0],
    [(1, 1), 1]
]


if __name__ == "__main__":

    weights, bias = train(train_set, epoch = 10)
    print("Weights: ")
    print(weights)
    print("Bias: ", bias)

    i = 0
    for input in val_set:
        i += 1
        print("Val set number ", i, ":")
        print(input, " --> ", perceptron(weights, bias, input))

    loss = utils.loss_fcn(weights, bias, test_set)
    print("Loss: ", loss)
