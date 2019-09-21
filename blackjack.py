from classes import DeckOfCards, Player
from functions import print_player_cards, title, make_bet, separator, \
    input_money
from typing import Tuple

game: bool = True
bet: int = 0
chips: Tuple[int, ...] = (1, 5, 25, 50, 100, 500, 1000)

card_suits = (('\033[0;30;47m' + chr(9824) + '\033[0m'),
              ('\033[0;31;47m' + chr(9830) + '\033[0m'),
              ('\033[0;31;47m' + chr(9829) + '\033[0m'),
              ('\033[0;30;47m' + chr(9827) + '\033[0m'))

cards = (('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
         ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10), ('A', 11))

player_title, dealer_title = 'Ваши карты', 'Карты дилера'

dealer = Player([DeckOfCards(cards, card_suits)])
player = Player([DeckOfCards(cards, card_suits),
                 DeckOfCards(cards, card_suits)])

separator()
money: int = input_money()
print(money)

while game:
    available_chips: Tuple[int, ...] = tuple(c for c in chips if money >= c)

    print('\nВыберите фишку и укажите номер фишки.\n')
    bet = make_bet(available_chips)
    print(bet)
    money -= bet

    print(money)

    continue_game = input('Продолжить игру? (y/n)\n>>> ')
    game = True if continue_game == 'y' else False
