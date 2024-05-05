# Description: This script is used to convert the images in the dataset folder to 256x256 pixels and save them in the processed_images folder
import os
from PIL import Image
import numpy as np
import multiprocessing as mp

resultPath = "processed_images_test/" #path to save the processed images
originPath = "test_dataset/" #path to the dataset folder


def convert_to_square(image_path,character, id): #convert the image to a square image and save it in the processed_images folder
    img = Image.open(image_path) #open the image
    img = img.resize((128, 128)) #resize the image to 256x256 pixels
    img.save(resultPath + character + "/" + str(id) + ".png") #save the image in the processed_images folder   

if __name__ == "__main__":
    
    characters = os.listdir(originPath) #get the list of characters in the dataset folder
    for character in characters: #loop through each character
        print(f"===================={character}====================")
        try: #Try to create a folder for the character if it does not exist
            os.mkdir(resultPath + character)
        except FileExistsError: #If the folder already exists, skip creating the folder
            print(f"{character} folder already exists")	
            pass
        
        try: #Check if the processed_images folder for the character already has the same number of images as the dataset folder
            
            if len(os.listdir(resultPath + character)) == len(os.listdir(originPath + character)):
                print(f"{character} folder already has processed images")
                continue
        except Exception as e:
            pass

        try: #Check if the value in the character variable is a directory
            images = os.listdir(originPath + character)
        except NotADirectoryError:
            print(f"{character} is not a directory")
            continue
        
        pool = mp.Pool(mp.cpu_count()) #Create a pool of processes
        print(f"Processing {len(images)} images in {mp.cpu_count()} threads")
        for i, image in enumerate(images): #loop through the images in the character folder to assign the images to a worker in the pool
            id = str(i).zfill(3) #format the id to have 3 digits
            pool.apply_async(convert_to_square, args=(originPath + character + "/" + image, character, id)) 
        pool.close() #close the pool
        pool.join() #wait for all the workers to finish processing the images
        print(f"Finished processing {character} images in {mp.cpu_count()} threads")

