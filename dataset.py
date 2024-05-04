import torch
from torch.utils.data import Dataset
from torchvision.transforms import Compose
import os
from PIL import Image

class GenshinDataSet(Dataset):
    def __init__(self, directory: str, transforms: Compose = None) -> None:
        self.directory = directory  # path to the dataset directory
        self.characters = os.listdir(directory)  # List of characters as folder names
        self.transforms = transforms  # Image transformations
        self.images = []  # List of image paths
        self.labels = []  # List of labels (numerical)

        for character in self.characters:  # Loop through the list of characters to get the images and labels
            category_path = os.path.join(directory, character)  # Path to the character folder
            label = len(self.characters) - 1 - self.characters.index(character)  # Assign numerical label based on character index

            for image_file in os.listdir(category_path):  # Loop through the images in the character folder
                image_path = os.path.join(category_path, image_file)
                self.images.append(Image.open(image_path))                
                self.labels.append(label)  # Append numerical label

    def __getitem__(self, index) -> tuple[any, torch.Tensor]:  # Get the image and label at the specified index
        image = self.images[index]  # Get the image
        label = self.labels[index]  # Get the label

        if image.mode == 'L':  # Check for grayscale mode ('L')
                    image = image.convert('RGB')  # Convert to RGB mode
        
        if self.transforms is not None:
            image = self.transforms(image)

        return image, torch.tensor(label)  # Return the image and label as a tuple (image, torch.Tensor)

    def __len__(self) -> int:
        return len(self.images)  # Return the number of images in the dataset

    def getLabelCount(self) -> int:
        return len(self.characters)  # Return the number of characters in the dataset