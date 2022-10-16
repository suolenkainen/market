#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from ctypes import util
from PIL import Image
from utils import csv_to_dict_converter
from cards import generate_list_of_cards_from_source_data
import os
import random

PATH = os.path.abspath(os.getcwd())


folder = "C:\\Users\\pmarj\\OneDrive\\Documents\\Pekan korttipeli\\Art Work\\"


#Read the two images
image1 = Image.open(folder + "SF1-000.jpg")
image2 = Image.open(folder + "SF1-001.jpg")
image3 = Image.open(folder + "SF1-002.jpg")
image4 = Image.open(folder + "SF1-003.jpg")
image5 = Image.open(folder + "SF1-004.jpg")
#resize, first image
image1_size = image1.size
image2_size = image2.size
image3_size = image3.size
image4_size = image4.size
image5_size = image5.size
new_image = Image.new('RGB',(5*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.paste(image3,(2*image1_size[0],0))
new_image.paste(image4,(3*image1_size[0],0))
new_image.paste(image5,(4*image1_size[0],0))
# new_image.save(folder + "merged_image.jpg","JPEG")
# new_image.show()



set_cards = csv_to_dict_converter(PATH + "\\src\\resources\\cards_in_set.csv")

cards = generate_list_of_cards_from_source_data(set_cards)

booster_cards = []
for x in range(8):
    booster_card = random.choice(cards)
    booster_cards.append(booster_card)

for k, _card in enumerate(booster_cards):
    image = Image.open(folder + _card["SET_ID"] + ".jpg")
    image_size = image.size
    if k == 0:
        new_image = Image.new('RGB',(8*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image,(k*image_size[0],0))
new_image.show()