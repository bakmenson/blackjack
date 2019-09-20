from classes import DeckOfCards, Player
from functions import print_player_cards, title, make_bet, separator
from typing import Tuple

game: bool = True
money: int = 0
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

while game:
    separator()
    print('\n', 'Выберите фишку и укажите номер фишки (1-6).\n')
    while True:
        try:
            bet = make_bet(chips)
        except ValueError:
            print('\n Неверная команда. Укажите номер команды (1-6).\n')
            continue
        except IndexError:
            print('\n Неверная команда. Такой команды нет (1-6).\n')
            continue
        break

    continue_game = input(' Продолжить игру? (y/n)\n >>> ')
    game = True if continue_game == 'y' else False
