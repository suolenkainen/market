#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

import random
import copy
import math

decks = [["Island", True, [], [], 0, 0, 0, None, 1, "blue", "mana", 1],
        ["Island", True, [], [], 0, 0, 0, None, 1, "blue", "mana", 1],
        ["Forest", True, [], [], 0, 0, 0, None, 1, "green", "mana", 1],
        ["Forest", True, [], [], 0, 0, 0, None, 1, "green", "mana", 1],
        ["Hills", True, [], [], 0, 0, 0, None, 1, "red", "mana", 1],
        ["Hills", True, [], [], 0, 0, 0, None, 1, "red", "mana", 1],
        ["Desert", True, [], [], 0, 0, 0, None, 1, "yellow", "mana", 1],
        ["Desert", True, [], [], 0, 0, 0, None, 1, "yellow", "mana", 1],
        ["Striped Crab", True, [], ["green"], 1, 1, 1, "blue", 0, None, "creature", 1],
        ["Teall Archer", True, [], ["red"], 1, 1, 1, "blue", 0, None, "creature", 1],
        ["Raging Gwellyn", True, [], ["yellow"], 1, 1, 1, "blue", 0, None, "creature", 1],
        ["Tree-touched", True, [], ["blue"], 1, 1, 1, "green", 0, None, "creature", 1],
        ["Golden Rabbit", True, [], ["red"], 1, 1, 1, "green", 0, None, "creature", 1],
        ["Ellin Archer", True, [], ["yellow"], 1, 1, 1, "green", 0, None, "creature", 1],
        ["Badum Ogres", True, [], ["blue"], 1, 1, 1, "red", 0, None, "creature", 1],
        ["Badum Librarian", True, [], ["green"], 1, 1, 1, "red", 0, None, "creature", 1],
        ["Hunter-Killer", True, [], ["yellow"], 1, 1, 1, "red", 0, None, "creature", 1],
        ["Djinn Harlequin", True, [], ["blue"], 1, 1, 1, "yellow", 0, None, "creature", 1],
        ["Badland Guardian", True, [], ["green"], 1, 1, 1, "yellow", 0, None, "creature", 1],
        ["Star Gazer", True, [], ["red"], 1, 1, 1, "yellow", 0, None, "creature", 1],
        ["Rough Seas", True, [], ["green"], 1, 0, 1, "blue", 0, None, "enchantment", 1],
        ["Woodland Stride", True, [], ["red"], 1, 0, 1, "green", 0, None, "enchantment", 1],
        ["Rock Slide", True, [], ["yellow"], 1, 0, 1, "red", 0, None, "enchantment", 1],
        ["Wind in the Grass", True, [], ["blue"], 1, 0, 1, "yellow", 0, None, "enchantment", 1],
        ["Spirit of Teall", True, [], ["red"], 2, 2, 2, "blue", 0, None, "creature", 1],
        ["Mist Deva", True, [], ["yellow"], 2, 2, 2, "blue", 0, None, "creature", 1],
        ["Treelord", True, [], ["red"], 2, 2, 2, "green", 0, None, "creature", 1],
        ["Ellin Campers", True, [], ["blue"], 2, 2, 2, "green", 0, None, "creature", 1],
        ["Badum General", True, [], ["green"], 2, 2, 2, "red", 0, None, "creature", 1],
        ["Guarddog", True, [], ["yellow"], 2, 2, 2, "red", 0, None, "creature", 1],
        ["Storm Giant", True, [], ["green"], 2, 2, 2, "yellow", 0, None, "creature", 1],
        ["Black-tail Sparrow", True, [], ["blue"], 2, 2, 2, "yellow", 0, None, "creature", 1],
        ["Stone Shield", True, [], ["red"], 2, 0, 2, "blue", 0, None, "enchantment", 1],
        ["Roots of Wrath", True, [], ["yellow"], 2, 0, 2, "green", 0, None, "enchantment", 1],
        ["Hoard of Badum", True, [], ["blue"], 2, 0, 2, "red", 0, None, "enchantment", 1],
        ["Window", True, [], ["green"], 2, 0, 2, "yellow", 0, None, "enchantment", 1]]


class Card():
    def __init__(self, atributes):
        [id, name, active, conditions, preferred, attack, defence, cost, cost_type, mana, mana_type, type, attraction] = atributes
        self.id = id
        self.name = name
        self.active = active
        self.conditions = conditions
        self.abilities = []
        self.qualities = []
        self.preferred = preferred
        self.attack = attack
        self.defence = defence
        self.cost = cost
        self.cost_type = cost_type
        self.mana = mana
        self.mana_type = mana_type
        self.type = type
        self.attraction = attraction

class Player():
    def __init__(self, id):
        self.name = f"Player {id}"
        self.deck = []
        self.hand = []
        self.table = []
        self.discard = []
        self.health = 10


default_deck = []
id = 0

for c in decks:
    card = Card([id] + c)
    default_deck.append(card)
    id += 1

cycles = 0
while True:
    players = []

    for n in range(2):
        id = 0
        player = Player(n)
        owndeck = []
        for c in decks:
            card = Card([id] + c)
            owndeck.append(card)
            id += 1
        player.deck = copy.deepcopy(default_deck)
        topten = sorted(player.deck, key=lambda d: d.attraction, reverse=True)[:10]
        del player.deck[:7]
        random.seed(n + n*cycles)
        random.shuffle(player.deck)
        player.deck = topten + player.deck[:13]
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
            if not table_card.active:
                if "blocked" not in table_card.conditions:
                    table_card.active = True
                else:
                    table_card.active.condition.remove("blocked")

        # First play mana cards
        while True:            
            for k, card in enumerate(player.hand):
                if card.type == "mana":
                    player.table.append(player.hand.pop(k))
                    break
            if k == len(player.hand) - 1:
                break
        
        # Then play all possible cards from hand
        while True:            
            for k, card in enumerate(player.hand):
                if card.cost > 0:
                    inactivate_cards = []
                    manacost = card.cost
                    for m, manacard in enumerate(player.table):
                        if manacard.type == "mana" and card.cost_type == manacard.mana_type and manacard.active == True:
                            manacost -= manacard.mana
                            inactivate_cards.append(m)
                        if manacost == 0:
                            for c in inactivate_cards:
                                player.table[c].active = False
                            if card.type != "enchantment":
                                card.active = False
                            player.table.append(player.hand.pop(k))
                            break
            if k == len(player.hand) - 1:
                break
        if player.table == []:
            break

        # Then attack enemy with each available card
        # If card is enchantment, it is destroyed after use
        s = True
        while s == True:
            for k, card in enumerate(player.table):
                if card.attack == 0 or card.active == False:
                    continue
                attack_e = None
                for e, e_card in enumerate(enemy.table):
                    if e_card.defence > 0 and e_card.defence <= card.attack:
                        attack_e = e
                        if e_card.cost_type in card.preferred:
                            enemy.discard.append(enemy.table.pop(e))
                            player.table[k].active == False
                            if card.type == "enchantment":
                                player.discard.append(player.table.pop(k))
                            break
                    if attack_e != None:
                        enemy.discard.append(enemy.table.pop(e))
                        player.discard.append(player.table.pop(k))
                        break
                    if e == len(enemy.table) -1:
                        enemy.health -= card.attack
                        player.table[k].active == False
            if k == len(player.table) - 1:
                print(f"{cycles}")
                break

        finish = False
        winner = player.name
        if player.deck == [] or cycles in [1,2,3,4,5] or player.health < 1:
            print("Enemy won")
            finish = True
            winner = enemy.name
        if enemy.health < 1 or finish:
            print(f"{winner} IS VICTORIOUS!! on cycle {cycles}")
            player.deck += player.hand + player.discard + player.table
            enemy.deck += enemy.hand + enemy.discard + enemy.table
            for card in player.deck:
                card.attraction = 2.00
            for card in enemy.deck:
                card.attraction = 0.50
            all_deck_cards = player.deck + enemy.deck
            for ids in all_deck_cards:
                for card_id in default_deck:
                    if ids.id == card_id.id:
                        card_id.attraction = round(math.sqrt(ids.attraction * card_id.attraction), 2)
                        break
            printdeck = sorted(default_deck, key=lambda d: d.attraction, reverse=True)

            break
        if attacker == 1:
            attacker = 0
            defender = 1
        else:
            attacker = 1
            defender = 0
    cycles += 1
    if cycles == 500:
        for n in printdeck[:20]:
            print(n.name, n.attraction, n.attack, n.defence, n.cost, n.cost_type)
        break


if __name__ == '__main__':
    pass