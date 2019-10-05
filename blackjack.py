from typing import Tuple, Any
from os import get_terminal_size, system, name
from deck import Deck
from player import Player
from functions import form_cards, title, make_bet, separator, \
    input_money, is_continue, print_player_cards

term_width: int = get_terminal_size()[0]
clear: str = 'cls' if name == 'nt' else 'clear'

chips: Tuple[int, ...] = (1, 5, 25, 50, 100, 500, 1000)

card_suits = ('\x1b[0;30;47m' + chr(9824) + '\x1b[0m',
              '\x1b[0;31;47m' + chr(9830) + '\x1b[0m',
              '\x1b[0;31;47m' + chr(9829) + '\x1b[0m',
              '\x1b[0;30;47m' + chr(9827) + '\x1b[0m')

face_cards = (
    (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, 7), (8, '8'),
    (9, '9'), (10, '10'), (10, 'J'), (10, 'Q'), (10, 'K'), (11, 'A')
)

# face_cards = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
# card_values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)

# get 4 face_cards for each card_suits
cards: Tuple[Any, ...] = tuple(
    (*i[0], i[1])
    for card in (zip((_,) * 4, card_suits) for _ in face_cards)
    for i in card
)

deck = Deck(cards)
dealer = Player(deck.get_card())
player = Player(deck.get_card(2))

system(clear)
separator(term_width)

# print('\x1b[10B')

money: int = input_money(term_width)

bet: int = 0
bets: Tuple[int, ...] = ()
insurance: int = 0

# game
while True:

    # make a bet
    while True:
        system(clear)
        separator(term_width)
        print(f"{'Сделайте ставку (укажите номер фишки).':^{term_width}}\n")
        bet = make_bet(chips, money, term_width)
        bets += (bet,)
        money -= bets[-1]

        separator(term_width)
        if money and is_continue('Сделать еще ставку', term_width):
            continue
        break

    sum_bets: int = sum(bets)

    # print dealer cards
    system(clear)
    title('Dealer Cards', term_width)
    print_player_cards(form_cards(dealer.get_player_cards()), term_width)
    print(f"{'':>{int(term_width / 3)}}{'Score: '}{dealer.get_cards_value}")

    # print player cards
    title('Your Cards', term_width)
    while True:
        print_player_cards(form_cards(player.get_player_cards()), term_width)
        print(f"{'':>{int(term_width / 3)}}{'Score: '}"
              f"{player.get_cards_value}")

        if is_continue('Continue', term_width):
            print('\x1b[11A')
            player.add_card(deck.get_card())
            continue
        break

    separator(term_width)
    if money and is_continue('Продолжить игру', term_width):
        player.remove_cards(), dealer.remove_cards()
        player.add_card(deck.get_card(2)), dealer.add_card(deck.get_card())
        continue
    break
