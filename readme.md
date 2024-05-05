# Genshin Image Classifier
> A simple image classifier trained on 20 classes of Genshin Impact characters, using a custom Convolutional Neural Network (CNN) architecture.
## Introduction
This project is a simple image classifier trained on 20 classes of Genshin Impact characters. The dataset was obtained from web scraping images from [Pixiv.net](https://www.pixiv.net/) using the tags of each 20 characters. The dataset consists of 5974 images, with each class having around 300 images. The images were preprocessed resized to 128x128 pixels and normalized. The model was trained using a custom Convolutional Neural Network (CNN) architecture. The model was trained for 200 epochs with a batch size of 64. The model achieved an accuracy of 0.85 on the validation set. The model was then tested on a separate test set and achieved an accuracy of 0.35. The model is available as a Pretained Model in huggingface as [genshin-image-classifier](https://huggingface.co/<add-link>).

## Bias
As the images were obtained by web scraping by the tags of each character, the dataset may contain bias towards the images that despite being tagged with the character's name, may not actually be the character, either because the first image was not the character or the image was not tagged correctly. Also some images may contain multiple characters, which may cause the model to predict the wrong character. 

## Model
TODO: Add model architecture and training details

## Requirements
- A GPU with CUDA support
- Python 3.11
- CUDA 12.1
- Conda

## Installation
1. Clone the repository
```bash
git clone https://github.com/02loveslollipop/GenshinImageClassifier
```	
2. Create conda environment
```bash
conda env create -f environment.yml
```
3. Activate conda environment
```bash
conda activate genshin-image-classifier
```
4. TODO: Implement local deployment

