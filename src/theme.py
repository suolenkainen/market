#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output


def connect_cards_to_a_theme(cards, theme, card_theme_connections):
    theme_type = theme["THEME_TYPE"]
    for _card in cards:
        _connection = {"CARD_ID": _card["ID"], "THEME_ID": theme["ID"], "ATTRACTION": theme["GENERAL_ATTRACTION"]}
        if _connection not in card_theme_connections and theme[theme_type] == _card[theme_type]:
            card_theme_connections.append(_connection)

    return card_theme_connections


if __name__ == '__main__':
    check_output("python .\\src\\theme.py.test -v", shell=True)