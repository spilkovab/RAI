import torch
import torch.nn as nn
import torch.optim as optim

class Perceptron(nn.Module):
    """ CONSTRUCTOR OF THE PERCEPTRON CLASS """

    def __init__(self, input_size):
        """ Constructor of the parent"""
        super(Perceptron, self).__init__()

        # Network architecture
        # fc = fully connected layer (muzu pojmenovat jak chci)
        # Linearni, vstup = vahy, 1 = jeden vystup
        self.fc = nn.Linear(input_size, 1)

    def forward(self, x):
        """ vezmu vstup, prepocitam/prozenu sigmoidou a vratim jako vystup"""
        y = self.fc(x)
        return torch.sigmoid(y)
    
# set the model
model = Perceptron(2)

# tensor from array for in/out
inputs = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
outputs = torch.tensor([[0], [0], [0], [1]], dtype = torch.float32)

criterion = nn.MSELoss()
optimization = optim.SGD(model.parameters(), lr=0.1)        # !!! jak ma pracovat se ztratovou funkci aby menil vahy

# training
epochs = 2000
for epoch in range(epochs):
    y = model(inputs)
    loss = criterion(y, outputs)
    optimization.zero_grad()            # !!!
    loss.backward()
    optimization.step()                 # !!!

    print("Epoch: ", epoch, "/", epochs)
    print("Loss: ", loss.item())

    


with torch.no_grad():
    """ toto funguje basically jako try-catch """

    prediction = model(torch.tensor([[0, 0]], dtype=torch.float32))
    print("[0, 0] -> ", prediction.item())