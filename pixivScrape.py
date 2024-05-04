# Description: This script scrapes images from pixiv based on a list of tags and retrieves n images for each tag. The images are saved in a folder named after the tag in the dataset folder.
from pixivpy3 import *
import multiprocessing as mp
import os
import yaml


with open("token.yaml", "r") as file: # Load the access token and refresh token from token.yaml
    token = yaml.safe_load(file)
    access_token = token["access_token"]
    refresh_token = token["refresh_token"]

api = AppPixivAPI() # Initialize the Pixiv API
api.set_auth(access_token=access_token, refresh_token=refresh_token) # Set the authentication tokens

offset = 300 # Offset for the images
n = 90 # Number of images to download for each character
resultFolder = "test_dataset" # Folder to save the images

if resultFolder == "": # If the result folder is not specified, save the images in the root directory of the script
    path = resultFolder
else: # If the result folder is specified, save the images in the specified folder  
    if resultFolder not in os.listdir(): # Check if the folder exists, if not, create the folder
        os.mkdir(resultFolder)
    path = f"{resultFolder}/" # Set the path to the specified folder

genshin_characters = [ # List of Genshin Impact characters to search for
    "アルレッキーノ(原神)", # Arlechino
    "フリーナ", # Furina
    "雷電将軍", # Raiden Shogun
    "八重神子", # Guuji Yae
    "神里綾華",  # Kamisato Ayaka
    "千織(原神)", # Chiori
    "シュヴルーズ", # Chevreuse
    "シャルロット(原神)", # Charlotte
    "甘雨(原神)", # Ganyu
    "胡桃(原神)", # Hu Tao
    "刻晴", # Keqing
    "ニィロウ", # Nilou
    "ナヴィア", # Navia
    "珊瑚宮心海", # Sangonomiya Kokomi
    "煙緋", # Yanfei
    "夜兰", # Yelan
    "ノエル(原神)", # Noel
    "スクロース(原神)", # Sucrose
    "ディシア", # Dehya
    "ジン(原神)" #Jean
]

genshin_characters_map = { # Mapping of Genshin Impact characters to their corresponding folder names
    "アルレッキーノ(原神)": "Arlechino",
    "フリーナ": "Furina",   
    "雷電将軍": "Raiden Shogun",
    "八重神子": "Guuji Yae",
    "神里綾華": "Kamisato Ayaka",
    "千織(原神)": "Chiori",
    "シュヴルーズ": "Chevreuse",
    "シャルロット(原神)": "Charlotte",
    "甘雨(原神)": "Ganyu",
    "胡桃(原神)": "Hu Tao",
    "刻晴": "Keqing",
    "ニィロウ": "Nilou",
    "ナヴィア": "Navia",
    "珊瑚宮心海": "Sangonomiya Kokomi",
    "煙緋": "Yanfei",
    "夜兰": "Yelan",
    "ノエル(原神)": "Noel",
    "スクロース(原神)": "Sucrose",
    "ディシア": "Dehya",
    "ジン(原神)": "Jean"
}

for character in genshin_characters: # Loop through the list of Genshin Impact characters to download images for each character
    print(f"===================={character}====================")
    count = offset # Initialize the count of downloaded images for the character
    try: # Try to create a folder for the character if it does not exist
        os.mkdir(f"{path}{genshin_characters_map[character]}")
    except FileExistsError:
        print(f"{genshin_characters_map[character]} folder already exists")
        pass

    if len(os.listdir(f"{path}{genshin_characters_map[character]}")) == n: # Check if the folder already has n images and skip the character
        print(f"{genshin_characters_map[character]} folder already has {n} images")
        continue
    elif len(os.listdir(f"{path}{genshin_characters_map[character]}")) > 0: # Check if the folder already has images and resume downloading from that state
        print(f"Resuming download for {genshin_characters_map[character]}")
        count = len(os.listdir(f"{path}{genshin_characters_map[character]}"))
    
    while count < (n + offset): # Loop until n images are downloaded for the character
        try:
            json_result = api.search_illust(character,sort="popular_desc",req_auth=True,offset=count) # request the images from pixiv based on the tag
            
            if json_result.illusts == []: # If no images are found for the tag, break the loop
                break
            
            for illust in json_result.illusts: # Loop through the images and download them
                url = illust.image_urls.medium # Get the image URL
                api.download(url, path=f"{path}{genshin_characters_map[character]}") # Download the image
                count += 1 # Increment the count of downloaded images
            print(count) # Print the count of downloaded images
        
        except TypeError as e:
            print(e)

    
