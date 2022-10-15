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
            individual_card['ID'] =  running_id
            individual_card['SET_ID'] = _card_element['SET_ID']
            individual_card['SET'] = _card_element['SET']
            individual_card['COLOUR'] = _card_element['COLOUR'] 
            individual_card['NAME'] = _card_element['NAME']
            individual_card['TYPE'] = _card_element['TYPE']
            individual_card['ATTRIBUTE'] = _card_element['ATTRIBUTE']
            individual_card['RARITY'] = _card_element['RARITY']
            individual_card['ARTIST'] = _card_element['ARTIST'] 
            individual_card['DESCRIPTION'] = _card_element['DESCRIPTION']

            if _card_element['NORMAL_AMOUNT'] != 0:
                individual_card['SPECIAL'] = 'Normal'
                _card_element['NORMAL_AMOUNT'] -= 1
            elif _card_element['FOIL_AMOUNT'] != 0:
                individual_card['SPECIAL'] = 'Foil'
                _card_element['FOIL_AMOUNT'] -= 1
            elif _card_element['HOLOGRAM_AMOUNT'] != 0:
                individual_card['SPECIAL'] = 'Hologram'
                _card_element['HOLOGRAM_AMOUNT'] -= 1
            elif _card_element['GOLD_AMOUNT'] != 0:
                individual_card['SPECIAL'] = 'Gold'
                _card_element['GOLD_AMOUNT'] -= 1
            else:
                break
            list_of_individual_cards.append(individual_card)
            running_id += 1

    return list_of_individual_cards


if __name__ == '__main__':
    check_output("python .\\src\\cards.py.test -v", shell=True)