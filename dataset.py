import torch
from torch.utils.data import Dataset
from torchvision.transforms import Compose
import os
import cv2

class GenshinDataSet(Dataset):
    def __init__(self, directory: str, transforms: Compose =None ) -> None:
        self.directory = directory
        self.characters = os.listdir(directory)
        self.transforms = transforms
        self.images = []
        self.labels = []
        
        # Load image paths and labels from your file structure (modify accordingly)
        for character in self.characters:
            category_path = os.path.join(directory, character)
            label = character  # Assuming category folder name represents the label

            for image_file in os.listdir(category_path):
                image_path = os.path.join(category_path, image_file)
                self.images.append(image_path)
                self.labels.append(label)


    def __getitem__(self, index) -> tuple[any, str]:
        image = cv2.imread(self.images[index])
        label = self.labels[index]

        if image.shape[-1] == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        if self.transforms:
            image = self.transforms(image)

        return image, label

    def __len__(self) -> int:
        return len(self.images)