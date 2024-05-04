# Description: Custom dataset class for loading images and labels from a directory
import torch
from torch.utils.data import Dataset
from torchvision.transforms import Compose
import os
import cv2

class GenshinDataSet(Dataset):
    def __init__(self, directory: str, transforms: Compose =None) -> None:
        self.directory = directory # path to the dataset directory
        self.characters = os.listdir(directory) # List of characters as folder names
        self.transforms = transforms # Image transformations
        self.images = [] # List of image paths
        self.labels = [] # List of labels
        
        for character in self.characters: # Loop through the list of characters to get the images and labels 
            category_path = os.path.join(directory, character) # Path to the character folder
            label = character  # the label is the name of the folder

            for image_file in os.listdir(category_path): # Loop through the images in the character folder
                image_path = os.path.join(category_path, image_file) 
                self.images.append(image_path) # Add the image path to the images list
                self.labels.append(label) # Add the label to the labels list    


    def __getitem__(self, index) -> tuple[any, str]: # Get the image and label at the specified index
        image = cv2.imread(self.images[index]) # Read the image
        label = self.labels[index] # Get the label

        if image.shape[-1] == 3: # cv2 may read the image in BGR format, convert it to RGB format
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        if self.transforms: # Apply the transformations to the image if provided
            image = self.transforms(image)

        return image, label # Return the image and label as a tuple

    def __len__(self) -> int:
        return len(self.images) # Return the number of images in the dataset that corresponds to the length of the dataset