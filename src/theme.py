#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output


def connect_cards_to_a_theme(cards, theme):
    return cards, theme


if __name__ == '__main__':
    check_output("python .\\src\\cards.py.test -v", shell=True)