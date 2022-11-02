#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

import random
import copy

decks = [["Island", True, [], [], 0, 0, 0, None, 1, "blue", "mana"],
        ["Island", True, [], [], 0, 0, 0, None, 1, "blue", "mana"],
        ["Island", True, [], [], 0, 0, 0, None, 1, "blue", "mana"],
        ["Forest", True, [], [], 0, 0, 0, None, 1, "green", "mana"],
        ["Forest", True, [], [], 0, 0, 0, None, 1, "green", "mana"],
        ["Forest", True, [], [], 0, 0, 0, None, 1, "green", "mana"],
        ["Hills", True, [], [], 0, 0, 0, None, 1, "red", "mana"],
        ["Hills", True, [], [], 0, 0, 0, None, 1, "red", "mana"],
        ["Hills", True, [], [], 0, 0, 0, None, 1, "red", "mana"],
        ["Desert", True, [], [], 0, 0, 0, None, 1, "yellow", "mana"],
        ["Desert", True, [], [], 0, 0, 0, None, 1, "yellow", "mana"],
        ["Desert", True, [], [], 0, 0, 0, None, 1, "yellow", "mana"],
        ["Striped Crab", True, [], ["green"], 1, 1, 1, "blue", 0, None, "creature"],
        ["Teall Archer", True, [], ["red"], 1, 1, 1, "blue", 0, None, "creature"],
        ["Raging Gwellyn", True, [], ["yellow"], 1, 1, 1, "blue", 0, None, "creature"],
        ["Tree-touched", True, [], ["blue"], 1, 1, 1, "green", 0, None, "creature"],
        ["Golden Rabbit", True, [], ["red"], 1, 1, 1, "green", 0, None, "creature"],
        ["Ellin Archer", True, [], ["yellow"], 1, 1, 1, "green", 0, None, "creature"],
        ["Badum Ogres", True, [], ["blue"], 1, 1, 1, "red", 0, None, "creature"],
        ["Badum Librarian", True, [], ["green"], 1, 1, 1, "red", 0, None, "creature"],
        ["Hunter-Killer", True, [], ["yellow"], 1, 1, 1, "red", 0, None, "creature"],
        ["Djinn Harlequin", True, [], ["blue"], 1, 1, 1, "yellow", 0, None, "creature"],
        ["Badland Guardian", True, [], ["green"], 1, 1, 1, "yellow", 0, None, "creature"],
        ["Star Gazer", True, [], ["red"], 1, 1, 1, "yellow", 0, None, "creature"],
        ["Rough Seas", True, [], ["green"], 1, 0, 1, "blue", 0, None, "enchantment"],
        ["Woodland Stride", True, [], ["red"], 1, 0, 1, "green", 0, None, "enchantment"],
        ["Rock Slide", True, [], ["yellow"], 1, 0, 1, "red", 0, None, "enchantment"],
        ["Wind in the Grass", True, [], ["blue"], 1, 0, 1, "yellow", 0, None, "enchantment"],
        ["Spirit of Teall", True, [], ["red"], 2, 2, 2, "blue", 0, None, "creature"],
        ["Mist Deva", True, [], ["yellow"], 2, 2, 2, "blue", 0, None, "creature"],
        ["Treelord", True, [], ["red"], 2, 2, 2, "green", 0, None, "creature"],
        ["Ellin Campers", True, [], ["blue"], 2, 2, 2, "green", 0, None, "creature"],
        ["Badum General", True, [], ["green"], 2, 2, 2, "red", 0, None, "creature"],
        ["Guarddog", True, [], ["yellow"], 2, 2, 2, "red", 0, None, "creature"],
        ["Storm Giant", True, [], ["green"], 2, 2, 2, "yellow", 0, None, "creature"],
        ["Black-tail Sparrow", True, [], ["blue"], 2, 2, 2, "yellow", 0, None, "creature"],
        ["Stone Shield", True, [], ["red"], 2, 0, 2, "blue", 0, None, "enchantment"],
        ["Roots of Wrath", True, [], ["yellow"], 2, 0, 2, "green", 0, None, "enchantment"],
        ["Hoard of Badum", True, [], ["blue"], 2, 0, 2, "red", 0, None, "enchantment"],
        ["Window", True, [], ["green"], 2, 0, 2, "yellow", 0, None, "enchantment"]]


class Card():
    def __init__(self):
        self.name = "Forest"
        self.activate = True
        self.conditions = []
        self.preferred = []
        self.attack = 0
        self.defence = 0
        self.cost = 0
        self.cost_type = None
        self.mana = 1
        self.mana_type = "green"
        self.instant = False

class Player():
    def __init__(self):
        self.name = "Player 1"
        self.deck = []
        self.hand = []
        self.table = []
        self.discard = []
        self.health = 10

players = []

for n in range(2):
    player = Player()
    player.deck = copy.deepcopy(decks)
    random.seed(n)
    random.shuffle(player.deck)
    players.append(player)

for player in players:
    for n in range(7):
        player.hand.append(player.deck.pop())

attacker = 0
defender = 1

while True:
    player = players[attacker]
    enemy = players[defender]
    player.hand.append(player.deck.pop())

    # Activate all cards
    for table_card in player.table:
        if not table_card[1]:
            if "blocked" not in table_card[2]:
                table_card[1] = True
            else:
                table_card[1].condition.remove("blocked")

    # First play mana cards
    while True:
        for k, card in enumerate(player.hand):
            if card[10] == "mana":
                player.table.append(player.hand.pop(k))
                break
        if k == len(player.hand) - 1:
            break
    
    # Then play all possible cards from hand
    while True:
        for k, card in enumerate(player.hand):
            if card[6] > 0:
                inactivate_cards = []
                manacost = card[6]
                for m, manacard in enumerate(player.table):
                    if manacard[10] == "mana" and card[7] == manacard[9] and manacard[1] == True:
                        manacost -= manacard[8]
                        inactivate_cards.append(m)
                    if manacost == 0:
                        for c in inactivate_cards:
                            player.table[c][1] = False
                        if card[10] != "enchantment":
                            card[1] = False
                        player.table.append(player.hand.pop(k))
                        break
        if k == len(player.hand) - 1:
            break

    # Then attack enemy with each available card
    # If card is enchantment, it is destroyed after use
    s = True
    while s == True:
        for k, card in enumerate(player.table):
            if card[4] == 0 or card[1] == False:
                continue
            attack_e = None
            for e, e_card in enumerate(enemy.table):
                if e_card[5] > 0 and e_card[5] <= card[4]:
                    attack_e = e
                    if e_card[7] in card[3]:
                        enemy.discard.append(enemy.table.pop(e))
                        player.table[k][1] == False
                        if card[10] == "enchantment":
                            player.discard.append(player.table.pop(k))
                        break
                if attack_e != None:
                    enemy.discard.append(enemy.table.pop(e))
                    player.discard.append(player.table.pop(k))
                    break
                if e == len(enemy.table) -1:
                    enemy.health -= card[4]
                    player.table[k][1] == False
        if k == len(player.table) - 1:
            break
        # for enemy_card in enemy.table:
        #     if table_card[3] == enemy_card[7]:
        #         attack_card = enemy.table



    if enemy.health < 1:
        print("PLAYER IS VICTORIOUS!!")
        break
    if attacker == 1:
        attacker = 0
        defender = 1
    else:
        attacker = 1
        defender = 0

if __name__ == '__main__':
    pass