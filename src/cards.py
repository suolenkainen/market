#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output


def generate_list_of_cards_from_source_data(data_dictionary):

    list_of_individual_cards = []
    running_id = 0
    
    # Convert dictionary into a detailed list of card dicts
    for _card_element in data_dictionary:
        while True:
            individual_card = {}
            individual_card['id'] =  running_id
            individual_card['set_id'] = _card_element['set_id']
            individual_card['set'] = _card_element['set']
            individual_card['colour'] = _card_element['colour'] 
            individual_card['name'] = _card_element['name']
            individual_card['type'] = _card_element['type']
            individual_card['attribute'] = _card_element['attribute']
            individual_card['rarity'] = _card_element['rarity']
            individual_card['artist'] = _card_element['artist'] 
            individual_card['description'] = _card_element['description']

            if _card_element['normal_amount'] != 0:
                individual_card['special'] = 'Normal'
                _card_element['normal_amount'] -= 1
            elif _card_element['foil_amount'] != 0:
                individual_card['special'] = 'Foil'
                _card_element['foil_amount'] -= 1
            elif _card_element['hologram_amount'] != 0:
                individual_card['special'] = 'Hologram'
                _card_element['hologram_amount'] -= 1
            elif _card_element['gold_amount'] != 0:
                individual_card['special'] = 'Gold'
                _card_element['gold_amount'] -= 1
            else:
                break
            list_of_individual_cards.append(individual_card)
            running_id += 1

    return list_of_individual_cards


if __name__ == '__main__':
    check_output("python .\\src\\cards.py.test -v", shell=True)