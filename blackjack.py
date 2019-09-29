from classes import Card, Player
from functions import print_player_cards, title, make_bet, separator, \
    input_money, is_continue
from typing import Tuple

chips: Tuple[int, ...] = (1, 5, 25, 50, 100, 500, 1000)

card_suits = (('\033[0;30;47m' + chr(9824) + '\033[0m'),
              ('\033[0;31;47m' + chr(9830) + '\033[0m'),
              ('\033[0;31;47m' + chr(9829) + '\033[0m'),
              ('\033[0;30;47m' + chr(9827) + '\033[0m'))

face_cards = (
    ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
    ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 11)
)

player_title, dealer_title = 'Ваши карты', 'Карты дилера'

dealer = Player([Card(face_cards, card_suits)])
player = Player([Card(face_cards, card_suits),
                 Card(face_cards, card_suits)])

separator()

# q = 'y'
# while q == 'y':
#     print_player_cards(player)
#     player.add_card(DeckOfCards(face_cards, card_suits))
#     print('Input')
#     q = input('some input >>> ')
#     print('\033[10A')
# print('\033[10B')

bet: Tuple[int, ...] = ()
bets: Tuple[int, ...] = ()
money: int = input_money()

while True:
    while True:
        bet = make_bet(chips, money)
        bets += (bet[0],)
        money -= bets[-1]

        separator()
        if money and is_continue('Сделать еще ставку'):
            continue
        break

    sum_bets: int = sum(bets)
    print(bet[1])

    separator()
    if money and is_continue('Продолжить игру'):
        continue
    break
