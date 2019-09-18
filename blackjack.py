from classes import DeckOfCards, Player
from functions import add_card, print_player_cards, title
from random import choice

game: bool = True

symbols = (('\033[0;30;47m' + chr(9824) + '\033[0m'),
           ('\033[0;31;47m' + chr(9830) + '\033[0m'),
           ('\033[0;31;47m' + chr(9829) + '\033[0m'),
           ('\033[0;30;47m' + chr(9827) + '\033[0m'))

cards = (('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
         ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 11))

pl = Player([DeckOfCards(cards, symbols), DeckOfCards(cards, symbols)])
dl = Player([DeckOfCards(cards, symbols)])

print()
title('Dialler\'s Cards')
title('Player\'s Cards')

print_player_cards(pl)
