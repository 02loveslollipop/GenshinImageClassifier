'''Convert the dataset images to square images of size 256x256 stretched to fit the square shape'''

import os
from PIL import Image
import numpy as np
import multiprocessing as mp



def convert_to_square(image_path,character, id):
    img = Image.open(image_path)
    img = img.resize((256, 256))
    img.save("processed_images/" + character + "/" + str(id) + ".png")

if __name__ == "__main__": #the images are in the dataset folder where each character has a folder with their images
    
    characters = os.listdir("dataset")
    for character in characters:
        print(f"===================={character}====================")
        try:
            os.mkdir("processed_images/" + character)
        except FileExistsError:
            print(f"{character} folder already exists")	
            pass
        
        try:
            #check if the folder has been processed
            if len(os.listdir("processed_images/" + character)) == len(os.listdir("dataset/" + character)):
                print(f"{character} folder already has processed images")
                continue
        except Exception as e:
            pass

        try:
            images = os.listdir("dataset/" + character)
        except NotADirectoryError:
            print(f"{character} is not a directory")
            continue
        
        pool = mp.Pool(mp.cpu_count())
        print(f"Processing {len(images)} images in {mp.cpu_count()} threads")
        for i, image in enumerate(images):
            id = str(i).zfill(3)
            pool.apply_async(convert_to_square, args=("dataset/" + character + "/" + image, character, id)) 
        pool.close()
        pool.join()
        print(f"Finished processing {character} images in {mp.cpu_count()} threads")

