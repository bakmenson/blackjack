from classes import DeckOfCards, Player
from functions import print_player_cards, title

game: bool = True

card_suits = (('\033[0;30;47m' + chr(9824) + '\033[0m'),
              ('\033[0;31;47m' + chr(9830) + '\033[0m'),
              ('\033[0;31;47m' + chr(9829) + '\033[0m'),
              ('\033[0;30;47m' + chr(9827) + '\033[0m'))

cards = (('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
         ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 11))

player_title, dialler_title = 'Player\'s Cards', 'Dialler\'s Cards'

dialler = Player([DeckOfCards(cards, card_suits)])
player = Player([DeckOfCards(cards, card_suits),
                 DeckOfCards(cards, card_suits)])
