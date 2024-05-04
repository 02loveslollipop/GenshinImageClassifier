from pixivpy3 import *
import multiprocessing as mp
import os
import yaml

#get the access token and refresh token from token.yaml
with open("token.yaml", "r") as file:
    token = yaml.safe_load(file)
    access_token = token["access_token"]
    refresh_token = token[c]

api = AppPixivAPI()
api.set_auth(access_token=access_token, refresh_token=refresh_token)

n = 300

genshin_characters = [
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

genshin_characters_map = {
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

for character in genshin_characters:
    print(f"===================={character}====================")
    count = 0
    try:
        os.mkdir(genshin_characters_map[character])
    except FileExistsError:
        print(f"{genshin_characters_map[character]} folder already exists")
        pass

    if len(os.listdir(genshin_characters_map[character])) == n:
        print(f"{genshin_characters_map[character]} folder already has {n} images")
        continue
    elif len(os.listdir(genshin_characters_map[character])) > 0:
        print(f"{genshin_characters_map[character]} folder already has {len(os.listdir(genshin_characters_map[character]))} images, resuming download")
        count = len(os.listdir(genshin_characters_map[character]))
    
    while count < n:
        try:
            json_result = api.search_illust(character,sort="popular_desc",req_auth=True,offset=count)
            
            if json_result.illusts == []:
                break
            
            for illust in json_result.illusts:
                url = illust.image_urls.medium
                api.download(url, path=genshin_characters_map[character])
                count += 1
            print(count)
        
        except TypeError as e:
            print(e)

    
