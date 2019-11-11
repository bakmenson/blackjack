from typing import Tuple, Union, List
from deck import Deck
from player import BasePlayer, Player
from functions import term_width, forming_cards, title, make_bet, separator, \
    input_money, is_continue, print_player_cards, get_actions, choose_action, \
    print_player_info, clear_terminal

clear_terminal()
separator()
player_name = str()
while True:
    try:
        player_name = input(f"{'':>{int(term_width / 2 - 14)}}"
                            f"Enter your name >>> ")
        if not player_name or player_name == ' ' or player_name.isdigit():
            raise ValueError
    except ValueError:
        print(f"{'':>{int(term_width / 2 - 14)}}Incorrect player name")
        continue
    break

deck = Deck()
dealer = BasePlayer('dealer')
player = Player('tom')

separator()

# print('\x1b[10A')
# print('\x1b[10B')

money: Union[int, float] = input_money()

chips: List[int] = [1, 5, 25, 50, 100, 500, 1000]
bet: Union[int, float] = 0
bets: Tuple[Union[int, float], ...] = ()
cards_index: int = 0
insurance: Union[int, float] = 0
is_insurance: bool = False
is_double_down: bool = False
blackjack: bool = False
stop_game: bool = False
surrender: bool = False
is_split: bool = False

# game
while True:
    # players takes cards
    player.cards = deck.get_card(2)
    dealer.cards = deck.get_card()

    # make a bet
    while True:
        clear_terminal()
        separator()

        available_chips: List[Union[int, float]] = [
            *(chip for chip in chips if money >= chip), money
        ]

        print(f"{'Make a bet (select chip number).':^{term_width}}\n")
        for number, chip in enumerate(available_chips, start=1):
            if number == len(available_chips):
                print(
                    f'{number:>{int(term_width / 3 + 1)}}. All-in ({chip})'
                )
                break
            print(f'{number:>{int(term_width / 3 + 1)}}. {chip}')

        bet = make_bet(available_chips)
        bets += (bet,)
        money -= bets[-1]
        sum_bets: Union[int, float] = sum(bets)

        separator()
        print(f"{'':>{int(term_width / 3)}}Your bet: {sum_bets}")
        if money and is_continue('Add chip'):
            continue
        break

    # print dealer cards
    clear_terminal()
    print()
    title(dealer.get_name)
    for dealer_card in dealer.cards:
        print_player_cards(forming_cards(dealer_card))
    print(f"{'':>{int(term_width / 3)}}Score: {dealer.get_score()}")

    # player part game
    title(player.get_name)
    while cards_index < len(player):
        for player_card in player.cards[cards_index:]:
            print_player_cards(forming_cards(player_card))
            print_player_info(
                player.get_score(cards_index),
                sum_bets,
                money,
                insurance
            )

            # check if player has blackjack with 2 cards
            if player.get_score(0) == 21 and len(player) == 1:
                if dealer.get_score() == 11:
                    print(
                        f"{'':>{int(term_width / 3)}}{player.get_name.title()}"
                        f" has blackjack but {dealer.get_name.title()}"
                        f" has first card Ace."
                    )
                    if not is_continue(
                            "Continue (y) or end the game"
                            " and take the bet back (n)"
                    ):
                        money += sum_bets
                        stop_game = True
                        break
                elif dealer.get_score() < 10:
                    money += sum_bets * 1.5
                    blackjack = True
                    break
                else:
                    break

            if not blackjack and not stop_game and not is_double_down:
                if player.get_score(cards_index) >= 21:
                    break

                actions = get_actions(
                    player.get_score(cards_index),
                    player_card,
                    dealer.get_score(),
                    len(dealer),
                    money,
                    sum_bets,
                    is_double_down,
                    is_split,
                    is_insurance
                )

                # output actions list
                print()
                for number, action in enumerate(actions, start=1):
                    print(f"{'':>{int(term_width / 3)}}{number}. {action}")

                choice = choose_action(actions)

                if choice == 'Hit':
                    player.hit(deck.get_card(), cards_index)
                    cards_index -= 1
                    break
                elif choice == 'Surrender':
                    money += sum_bets / 2
                    surrender = True
                    break
                elif choice == 'Double down':
                    # player can choice double down one time per game
                    is_double_down = True
                    player.hit(deck.get_card(), cards_index)
                    money -= sum_bets
                    sum_bets *= 2
                    cards_index -= 1
                    break
                elif choice == 'Insurance':
                    # player can choice insurance one time per game
                    is_insurance = True
                    insurance += sum_bets / 2
                    continue
                elif choice == 'Split':
                    is_split = True
                    split_card: List = [
                        [player_card[1], *deck.get_card()],
                        [player_card[0], *deck.get_card()]
                    ]
                    player.split_cards(cards_index, split_card)
                    money -= sum_bets
                    sum_bets *= 2
                    cards_index -= 1
                    break
                else:
                    break
        cards_index += 1
    print(player.get_score_list)

    if not blackjack and not stop_game and not surrender:
        # dealer must taking cards until 17 score
        while dealer.get_score() < 17:
            dealer.hit(deck.get_card())

        clear_terminal()
        print()

        # print final dealer and player card
        title(dealer.get_name)
        for dealer_card in dealer.cards:
            print_player_cards(forming_cards(dealer_card))
        print(f"{'':>{int(term_width / 3)}}Score: {dealer.get_score()}")

        if not is_split:
            title(player.get_name)
            for card in player.cards:
                print_player_cards(forming_cards(card))

            print_player_info(
                player.get_score(0),
                sum_bets,
                money,
                insurance
            )
        else:
            title(player.get_name)
            print(f"{'':>{int(term_width / 3)}}"
                  f"{player.get_name.capitalize()}"
                  f" score list: {player.get_score_list}")

    separator()
    # show game result if was not split
    if blackjack or stop_game or surrender:
        if blackjack:
            print(f"{'':>{int(term_width / 3)}}{player.get_name.title()} "
                  f"win! Blackjack!\n")
        if stop_game:
            print(f"{'':>{int(term_width / 3)}}{player.get_name.title()} "
                  f"stopped the game and took the bet back.")
        if surrender:
            print(f"{'':>{int(term_width / 3)}}{player.get_name.title()} "
                  f"surrendered.")

    elif player.get_score() > 21 < dealer.get_score() \
            or 21 > player.get_score() == dealer.get_score() \
            or player.get_score() == 21 == dealer.get_score():
        money += sum_bets
        print(f"{'':>{int(term_width / 3)}}Push.\n")

    elif player.get_score() < 21 < dealer.get_score() \
            or player.get_score() == 21 < dealer.get_score() \
            or player.get_score() == 21 > dealer.get_score() \
            or 21 > player.get_score() > dealer.get_score():
        money += sum_bets * 1.5
        print(f"{'':>{int(term_width / 3)}}{player.get_name.title()} win!\n")
        if insurance:
            money -= insurance
            print(f"{'':>{int(term_width / 3)}}Lost insurance")

    else:
        if dealer.get_score() == 21 != player.get_score() \
                and len(dealer) == 2 and is_insurance:
            print(f"{'':>{int(term_width / 3)}}{player.get_name.title()} "
                  f"received insurance.\n")
            money += insurance * 2
        print(f"{'':>{int(term_width / 3)}}{dealer.get_name.title()} win.\n")

    # print player money after the game
    print(
        f"{'':>{int(term_width / 3)}}{player.get_name.title()}'s money: "
        f"{money}"
    )

    if money and is_continue('Continue the game'):
        # set default values if continue the game
        # player.cards, dealer.cards = [], []
        del player.cards
        del dealer.cards
        insurance, cards_index = 0, 0
        is_insurance, is_double_down, is_split = False, False, False
        blackjack, stop_game, surrender = False, False, False
        bets = ()
        continue
    break
