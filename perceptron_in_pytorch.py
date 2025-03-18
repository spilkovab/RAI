import torch
import torch.nn as nn
import torch.optim as optim

class Perceptron(nn.Module):
    """ CONSTRUCTOR OF THE PERCEPTRON CLASS"""

    def __init__(self, input_size):
        # Constructor of the parent
        super(Perceptron, self).__init__()

        # Network architecture
        # fc = fully connected layer (muzu pojmenovat jak chci)
        # Linearni, vstup = vahy, 1 = jeden vystup
        self.fc = nn.Linear(input_size, 1)

model = Perceptron(2)