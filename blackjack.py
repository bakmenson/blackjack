from typing import Tuple, Any, Union
from os import get_terminal_size, system, name
from deck import Deck
from player import Player
from functions import form_cards, title, make_bet, separator, \
    input_money, is_continue, print_player_cards, get_actions, choose_action, \
    print_player_info

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

system(clear)
separator(term_width)
player_name = str()
while True:
    try:
        player_name = input(f"{'':>{int(term_width / 2 - 14)}}"
                            f"Enter your name >>> ")
        if not player_name or player_name == ' ' or player_name.isdigit() \
                or player_name[0].isdigit():
            raise ValueError
    except ValueError:
        print(f"{'':>{int(term_width / 2 - 14)}}Incorrect player name")
        continue
    break

deck = Deck(cards)
dealer = Player('dealer')
player = Player(player_name)

separator(term_width)

# print('\x1b[10A')
# print('\x1b[10B')

money: Union[int, float] = input_money(term_width)

bet: Union[int, float] = 0
bets: Tuple[Union[int, float], ...] = ()
insurance: Union[int, float] = 0
insurance_count: int = 0
double_down_count: int = 0
blackjack: bool = False
stop_game: bool = False
surrender: bool = False

# game
while True:
    # players takes cards
    dealer.add_card(deck.get_card())
    player.add_card(deck.get_card(2))

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
    print()
    title(dealer.get_name(), term_width)
    print_player_cards(form_cards(dealer.get_cards()), term_width)
    print(f"{'':>{int(term_width / 3)}}Score: {dealer.get_scores}")

    # print player cards
    title(player.get_name(), term_width)
    while True:
        print_player_cards(form_cards(player.get_cards()), term_width)

        print_player_info(
            player.get_scores,
            sum_bets,
            money,
            insurance,
            term_width
        )

        # check if player has blackjack with 2 cards
        if player.get_scores == 21 and len(player.get_cards()) == 2:
            if dealer.get_scores == 11:
                print(
                    f"{'':>{int(term_width / 3)}}{player.get_name().title()} "
                    f"has blackjack but {dealer.get_name().title()} "
                    f"has first card Ace,"
                )
                q = f"continue (y) or end the game and take the bet back (n)"
                if not is_continue(q, term_width):
                    money += sum_bets
                    stop_game = True
                    break
            elif dealer.get_scores < 10:
                money += sum_bets * 1.5
                blackjack = True
                break
            else:
                break

        if not blackjack and not stop_game:
            if player.get_scores >= 21:
                break

            actions = get_actions(
                player.get_scores,
                player.get_cards(),
                dealer.get_scores,
                len(dealer.get_cards()),
                money,
                sum_bets,
                double_down_count,
                insurance_count
            )

            # output actions list
            print()
            for number, action in enumerate(actions, start=1):
                print(f"{'':>{int(term_width / 3)}}{number}. {action}")

            choice = choose_action(actions, term_width)

            if choice == 'Hit':
                player.add_card(deck.get_card())
                continue
            elif choice == 'Surrender':
                money += sum_bets / 2
                surrender = True
                break
            elif choice == 'Double down':
                # player can choice double down one time per game
                double_down_count += 1

                player.add_card(deck.get_card())
                money -= sum_bets
                sum_bets *= 2
                continue
            elif choice == 'Insurance':
                # player can choice insurance one time per game
                insurance_count += 1
                insurance += sum_bets / 2
                continue
            elif choice == 'Split':
                pass
            else:
                break

        break

    # dealer must taking cards until 17 score
    if not blackjack and not stop_game and not surrender:
        while dealer.get_scores < 17:
            dealer.add_card(deck.get_card())

        # print players cards and scores
        system(clear)
        print()

        title(dealer.get_name(), term_width)
        print_player_cards(form_cards(dealer.get_cards()), term_width)
        print(f"{'':>{int(term_width / 3)}}Score: {dealer.get_scores}")

        title(player.get_name(), term_width)
        print_player_cards(form_cards(player.get_cards()), term_width)

        print_player_info(
            player.get_scores,
            sum_bets,
            money,
            insurance,
            term_width
        )

    separator(term_width)
    # show game result if was not split
    if blackjack or stop_game or surrender:
        if blackjack:
            print(f"{'':>{int(term_width / 3)}}{player.get_name().title()} "
                  f"win! Blackjack!\n")
        if stop_game:
            print(f"{'':>{int(term_width / 3)}}{player.get_name().title()} "
                  f"stopped the game and took the bet back.")
        if surrender:
            print(f"{'':>{int(term_width / 3)}}{player.get_name().title()} "
                  f"surrendered.")

    elif player.get_scores > 21 < dealer.get_scores \
            or 21 > player.get_scores == dealer.get_scores \
            or player.get_scores == 21 == dealer.get_scores:
        money += sum_bets
        print(f"{'':>{int(term_width / 3)}}Push.\n")
        if insurance:
            print(f"{'':>{int(term_width / 3)}}Lost insurance")

    elif player.get_scores < 21 < dealer.get_scores \
            or player.get_scores == 21 < dealer.get_scores \
            or player.get_scores == 21 > dealer.get_scores \
            or 21 > player.get_scores > dealer.get_scores:
        money += sum_bets * 1.5
        print(f"{'':>{int(term_width / 3)}}{player.get_name().title()} win!\n")
        if insurance:
            money -= insurance
            print(f"{'':>{int(term_width / 3)}}Lost insurance")

    else:
        if dealer.get_scores == 21 != player.get_scores \
                and len(dealer.get_cards()) == 2 and insurance_count:
            print(f"{'':>{int(term_width / 3)}}{player.get_name().title()} "
                  f"received insurance.\n")
            money += insurance * 2
        print(f"{'':>{int(term_width / 3)}}{dealer.get_name().title()} win.\n")

    # print player money after the game
    print(
        f"{'':>{int(term_width / 3)}}{player.get_name().title()}'s money: "
        f"{money}"
    )

    if money and is_continue('Continue the game', term_width):
        # set default values if continue the game
        player.remove_cards(), dealer.remove_cards()
        insurance, insurance_count, double_down_count = 0, 0, 0
        blackjack, stop_game, surrender = False, False, False
        bets = ()
        continue
    break
