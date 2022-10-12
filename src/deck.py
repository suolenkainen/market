#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output


def connect_cards_to_decks(cards, decks, card_deck_connections):
    for _card in cards:
        for _deck in decks:
            if _deck["ACTIVE"] == False:
                continue
            _connection = {"CARD_ID": _card["ID"], "DECK_ID": _deck["ID"]}
            if _connection not in card_deck_connections:
                card_deck_connections.append(_connection)
    return card_deck_connections


def remove_card_deck_connection(cards, decks, card_deck_connections):
    for _card in cards:
        for _deck in decks:
            _connection = {"CARD_ID": _card["ID"], "DECK_ID": _deck["ID"]}
            if _connection in card_deck_connections:
                card_deck_connections.remove(_connection)
    return card_deck_connections


def release_deck(deck, date):

    if deck["RELEASE_DATE"] == "" and deck["ACTIVE"] == False:
        deck["RELEASE_DATE"] = date 
        deck["ACTIVE"] = True

    return deck


if __name__ == '__main__':
    check_output("python .\\src\\deck.py.test -v", shell=True)