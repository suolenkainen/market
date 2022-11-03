#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output

def awaken(target_card):
    if "blocked" in target_card.conditions:
        target_card.conditions.remove("blocked")
    target_card.active = True


def blocker(target_card): 
    if "blocked" not in target_card.conditions:
        target_card.conditions.append("blocked")
    target_card.active = False


def building(card):
    if card.attack != 0:
        card.attack = 0
    for ability in ["strenght", "haste", "rage", "rend"]:
        if ability in card.abilities:
            card.abilities.remove(ability)
    

def counter(): 
    pass


def curse(): 
    pass


def cycle(): 
    pass


def draw(): 
    pass


def draw2(): 
    pass


def draw3(): 
    pass


def equip(): 
    pass


def goad(): 
    pass


def haste(): 
    pass


def healing(): 
    pass


def healing2(): 
    pass


def healing3(): 
    pass


def healing4(): 
    pass


def instant(): 
    pass


def mana(): 
    pass


def rage(): 
    pass


def rend(): 
    pass


def resurrect(): 
    pass


def shield(): 
    pass


def strenght(): 
    pass


def wither(): 
    pass

if __name__ == '__main__':
    check_output("python .\\src\\game\\abilities.test.py -v", shell=True)