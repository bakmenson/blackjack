from classes import Deck, Player
from functions import form_cards, title, make_bet, separator, \
    input_money, is_continue, print_player_cards
from typing import Tuple, Generator, Iterator, Any
from os import get_terminal_size, system

term_width: int = get_terminal_size()[0]
chips: Tuple[int, ...] = (1, 5, 25, 50, 100, 500, 1000)

card_suits = ('\x1b[0;30;47m' + chr(9824) + '\x1b[0m',
              '\x1b[0;31;47m' + chr(9830) + '\x1b[0m',
              '\x1b[0;31;47m' + chr(9829) + '\x1b[0m',
              '\x1b[0;30;47m' + chr(9827) + '\x1b[0m')

face_cards = (
    (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, 7), (8, '8'),
    (9, '9'), (10, '10'), (10, 'J'), (10, 'Q'), (10, 'K'), (11, 'A')
)

# get 4 face_cards for each card_suits
cards: Tuple[Any, ...] = tuple(
    (*i[0], i[1])
    for card in (zip((_,) * 4, card_suits) for _ in face_cards)
    for i in card
)

deck = Deck(cards)

dealer = Player(deck.get_card())
player = Player(deck.get_card(2))

print()
print()
#print_player_cards(player)
#player.add_card(deck_of_card.get_card())

player.add_card(deck.get_card())

# for i in zip(*form_cards(player.get_player_cards())):
#     print(*i)

print_player_cards(form_cards(player.get_player_cards()), term_width)

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
