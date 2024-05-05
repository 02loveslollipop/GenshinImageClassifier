import torch
import torch.nn as nn

#input is a 128x128 image with 3 channels (RGB)
class ConvNet(nn.Module):
  def __init__(self,category_count):
    super(ConvNet,self).__init__()
    self.convolution_layer1 = nn.Conv2d(in_channels=3,out_channels=32,kernel_size=5) # Convolution layer 1: 3 input channels (RGB), 64 output channels (64 filters), 5x5 kernel size, output size = (128-5)/1 + 1 = 124
    self.convolution_layer2 = nn.Conv2d(in_channels=32,out_channels=32,kernel_size=5) # Convolution layer 2: 64 input channels (64 kernels from previous layer), 64 output channels (64 filters), 5x5 kernel size, output size = (124-5)/1 + 1 = 120
    self.max_pool = nn.MaxPool2d(kernel_size=2,stride=2) # Max pooling layer: 2x2 kernel size, stride 2 (reduces image size by 2, 120x120 to 60x60)

    self.convolution_layer3 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3) # Convolution layer 3: 64 input channels (64 kernels from previous layer), 128 output channels (128 filters), 3x3 kernel size, output size = (60-3)/1 + 1 = 58
    self.convolution_layer4 = nn.Conv2d(in_channels=64,out_channels=64,kernel_size=3) # Convolution layer 4: 128 input channels (128 kernels from previous layer), 128 output channels (128 filters), 3x3 kernel size, output size = (58-3)/1 + 1 = 56
    self.max_pool2 = nn.MaxPool2d(kernel_size=2,stride=2) # Max pooling layer 2: 2x2 kernel size, stride 2 (reduces image size by 2, 64x64 to 32x32), output size = 56/2 = 28
    self.convolution_layer5 = nn.Conv2d(in_channels=64,out_channels=128,kernel_size=3) # Convolution layer 5: 128 input channels (128 kernels from previous layer), 256 output channels (256 filters), 3x3 kernel size, output size = (28-3)/1 + 1 = 26
    self.convolution_layer6 = nn.Conv2d(in_channels=128,out_channels=128,kernel_size=3) # Convolution layer 6: 256 input channels (256 kernels from previous layer), 256 output channels (256 filters), 3x3 kernel size, output size = (26-3)/1 + 1 = 24
    self.max_pool3 = nn.MaxPool2d(kernel_size=2,stride=2) # Max pooling layer 3: 2x2 kernel size, stride 2 (reduces image size by 2, 32x32 to 16x16), output size = 24/2 = 12

    self.fully_connected1 = nn.Linear(128*12*12,4096) # Fully connected layer 1: 128*12*12 input features (128 filters from last convolution layer, 12x12 image size), 128 output features
    self.relu = nn.ReLU() # ReLU activation function
    self.fully_connected2 = nn.Linear(4096,1024) # Fully connected layer 2: 4096 inputs 1024 outputs)
    self.relu2 = nn.ReLU() # ReLU activation function
    self.fully_connected3 = nn.Linear(1024,512) # Fully connected layer 3: 1024 inputs 512 outputs)
    self.relu3 = nn.ReLU() # ReLU activation function
    self.fully_connected4 = nn.Linear(512,category_count) # Output layer: linear layer
    self.softmax = nn.Softmax(dim=1) # Softmax activation function

  def forward(self,x):
    output = self.convolution_layer1(x) # Convolution layer 1
    output = self.convolution_layer2(output) # Convolution layer 2
    output = self.max_pool(output) # Max pooling layer

    output = self.convolution_layer3(output) # Convolution layer 3
    output = self.convolution_layer4(output) # Convolution layer 4
    output = self.max_pool2(output) # Max pooling layer 2

    output = self.convolution_layer5(output) # Convolution layer 5
    output = self.convolution_layer6(output) # Convolution layer 6
    output = self.max_pool3(output) # Max pooling layer 3

    output = output.reshape(output.size(0),-1) # Flatten the output for the fully connected layer

    output = self.fully_connected1(output) # Fully connected layer 1
    output = self.relu(output)  # ReLU activation function
    output = self.fully_connected2(output) # Fully connected layer 2
    output = self.relu2(output) # ReLU activation function
    output = self.fully_connected3(output) # Fully connected layer 3
    output = self.relu3(output) # ReLU activation function
    output = self.fully_connected4(output) # Output layer
    output = self.softmax(output) # Softmax activation function
    return output