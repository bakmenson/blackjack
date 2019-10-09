from typing import Tuple, Any, Union
from os import get_terminal_size, system, name
from deck import Deck
from player import Player
from functions import form_cards, title, make_bet, separator, \
    input_money, is_continue, print_player_cards, get_actions, choose_action

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

# get 4 face_cards for each card_suits
cards: Tuple[Any, ...] = tuple(
    (*i[0], i[1])
    for card in (zip((_,) * 4, card_suits) for _ in face_cards)
    for i in card
)

deck = Deck(cards)
dealer = Player()
player = Player()

system(clear)
separator(term_width)

# print('\x1b[10B')

money: Union[int, float] = input_money(term_width)

bet: Union[int, float] = 0
insurance: Union[int, float] = 0
double_count: int = 0

# game
while True:
    player.add_card(deck.get_card(2))
    dealer.add_card(deck.get_card())

    bets: Tuple[Union[int, float], ...] = ()

    # make a bet
    while True:
        system(clear)
        separator(term_width)

        available_chips: Tuple[Union[int, float], ...] = tuple(
            chip for chip in chips if money >= chip
        )
        available_chips += (money,)

        print(f"{'Make a bet (select chip number).':^{term_width}}\n")
        for number, chip in enumerate(available_chips, start=1):
            if number == len(available_chips):
                print(
                    f'{number:>{int(term_width / 3 + 1)}}. All-in ({chip})'
                )
                break
            print(f'{number:>{int(term_width / 3 + 1)}}. {chip}')

        bet = make_bet(available_chips, term_width)
        bets += (bet,)
        money -= bets[-1]
        sum_bets: Union[int, float] = sum(bets)

        separator(term_width)
        print(f"{'':>{int(term_width / 3)}}Your bet: {sum_bets}")
        if money and is_continue('Add chip', term_width):
            continue
        break

    # print dealer cards
    system(clear)
    title('Dealer Cards', term_width)
    print_player_cards(form_cards(dealer.get_cards()), term_width)
    print(f"{'':>{int(term_width / 3)}}Score: {dealer.get_scores}")

    # print player cards
    title('Your Cards', term_width)
    while True:
        print_player_cards(form_cards(player.get_cards()), term_width)
        print(f"{'':>{int(term_width / 3)}}Score: {player.get_scores}")

        # actions(player.get_scores, player.get_cards(), term_width)

        # if is_continue('Continue', term_width):
        #     print('\x1b[12A')
        #     player.add_card(deck.get_card())
        #     continue
        actions = get_actions(
            player.get_scores,
            player.get_cards(),
            money, sum_bets,
            double_count
        )

        # output actions list
        for number, action in enumerate(actions, start=1):
            print(f"{'':>{int(term_width / 3)}}{number}. {action}")

        choice = choose_action(actions, term_width)

        if choice == 'Hit':
            player.add_card(deck.get_card())
            continue
        elif choice == 'Surrender':
            money += sum_bets / 2
            break
        elif choice == 'Double down':
            double_count += 1
            player.add_card(deck.get_card())
            sum_bets *= 2
            money -= sum_bets
            continue
        elif choice == 'Split':
            pass
        else:
            pass

        # print('\x1b[12A')
        break

    separator(term_width)
    if money and is_continue('Continue the game', term_width):
        player.remove_cards(), dealer.remove_cards()
        continue
    break
