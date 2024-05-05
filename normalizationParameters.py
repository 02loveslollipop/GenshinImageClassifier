#get the normalize parameters for the images in the dataset for each channel
import os
import cv2
import numpy as np
import multiprocessing as mp
import torch
from torchvision import transforms
from dataset import GenshinDataSet

all_transforms = transforms.Compose([transforms.ToTensor()
                                     ])
dataset = GenshinDataSet(directory='processed_images', transforms=all_transforms)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

def calculate_stats(dataloader):
    mean = torch.zeros(3)
    std = torch.zeros(3)
    n = 0
    for images, _ in dataloader:
        batch_mean = images.mean([0, 2, 3])  # Calculate mean across batch and spatial dimensions
        batch_std = images.std([0, 2, 3])  # Calculate standard deviation across batch and spatial dimensions
        mean += batch_mean
        std += batch_std
        n += images.size(0)  # Add number of images in the batch

    mean /= n
    std /= n
    return mean, std

mean, std = calculate_stats(dataloader)
print(f'Mean: {mean}')
print(f'Std: {std}')