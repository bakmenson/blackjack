from classes import Card, Player
from functions import print_player_cards, title, make_bet, separator, \
    input_money, is_continue
from typing import Tuple
from os import system
from os import get_terminal_size

term_width: int = get_terminal_size()[0]
chips: Tuple[int, ...] = (1, 5, 25, 50, 100, 500, 1000)

card_suits = ('\x1b[0;30;47m' + chr(9824) + '\x1b[0m',
              '\x1b[0;31;47m' + chr(9830) + '\x1b[0m',
              '\x1b[0;31;47m' + chr(9829) + '\x1b[0m',
              '\x1b[0;30;47m' + chr(9827) + '\x1b[0m')

face_cards = (
    ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
    ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 11)
)

cards = tuple(tuple(zip((i,) * 4, card_suits)) for i in face_cards)
deck = tuple((*i[0], i[1]) for card in cards for i in card)

for i in deck:
    print(i)

player_title, dealer_title = 'Ваши карты', 'Карты дилера'

dealer = Player((Card(face_cards, card_suits),))
player = Player((Card(face_cards, card_suits), Card(face_cards, card_suits)))

# system('clear')
#
# separator(term_width)
# q = 'y'
# while q == 'y':
#     print_player_cards(player, term_width)
#     player.add_card(Card(face_cards, card_suits))
#     print('Input')
#     q = input('some input >>> ')
#     print('\x1b[10A')
# print('\x1b[10B')
#
# separator(term_width)
# money: int = input_money()
#
# bet: int = 0
# bets: Tuple[int, ...] = ()
#
# while True:
#     while True:
#         system('clear')
#         separator(term_width)
#         print('Сделайте ставку (укажите номер фишки).')
#         bet = make_bet(chips, money, term_width)
#         bets += (bet,)
#         money -= bets[-1]
#
#         separator(term_width)
#         if money and is_continue('Сделать еще ставку'):
#             continue
#         break
#
#     sum_bets: int = sum(bets)
#
#     system('clear')
#     separator(term_width)
#     if money and is_continue('Продолжить игру'):
#         continue
#     break
