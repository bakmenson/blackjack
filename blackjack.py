from typing import Union, List
from webbrowser import open
from deck import Deck
from player import Player
from functions import term_width, forming_cards, player_title, make_bet, \
    separator, input_money, is_continue, print_player_cards, get_actions, \
    choose_action, print_player_info, clear_terminal

clear_terminal()
separator()

print(f"{'':>{int(term_width / 2 - 3)}}Welcome!")
print(f"{'':>{int(term_width / 2 - 11)}}Blackjack. Terminal Game.\n")
print(f"{'':>{int(term_width / 2 - 11)}}1. Start game.")
print(f"{'':>{int(term_width / 2 - 11)}}2. Read Wikipedia article.")

if choose_action(2) == 2:
    open('https://en.wikipedia.org/wiki/Blackjack')

player_name = str()
while True:
    try:
        player_name = input(f"\n{'':>{int(term_width / 2 - 11)}}"
                            f"Enter your name >>> ")
        if not player_name or player_name == ' ' or player_name.isdigit():
            raise ValueError
    except ValueError:
        print(f"{'':>{int(term_width / 2 - 11)}}Incorrect player name.")
        continue
    break

deck = Deck()
dealer = Player('dealer')
player = Player(player_name)

chips: List[int] = [1, 5, 25, 50, 100, 500, 1000]
total_bet: Union[int, float] = 0
cards_index: int = 0
surrender: List[int] = []
win: int = 0
push: int = 0
lose: int = 0
is_insurance: bool = False
is_double_down: bool = False
blackjack: bool = False
stop_game: bool = False
is_split: bool = False

separator()
player_money: Union[int, float] = input_money()

# the game
while True:
    # players takes cards
    player.cards = deck.get_card(2)
    dealer.cards = deck.get_card()

    # make a bet
    while True:
        clear_terminal()
        separator()

        available_chips: List[Union[int, float]] = [
            *(chip for chip in chips if player_money >= chip), player_money
        ]

        print(f"{'Make a bet (select chip number).':^{term_width}}\n")
        for number, chip in enumerate(available_chips, start=1):
            if number == len(available_chips):
                print(
                    f'{number:>{int(term_width / 3 + 1)}}. All-in ({chip})'
                )
                break
            print(f'{number:>{int(term_width / 3 + 1)}}. {chip}')

        bet: Union[int, float] = make_bet(available_chips)
        player_money -= bet
        total_bet += bet

        separator()
        print(f"{'':>{int(term_width / 3)}}Your bet: {total_bet}")
        if player_money and is_continue('Add chip'):
            continue
        break

    current_bet: Union[int, float] = total_bet

    # player part game
    while cards_index < len(player.cards):
        clear_terminal()
        print()

        # print dealer cards
        player_title(dealer.get_name)
        for dealer_card in dealer.cards:
            print_player_cards(forming_cards(dealer_card))
        print(f"{'':>{int(term_width / 3)}}Score: {dealer.get_score()}")

        # print player cards
        player_title(player.get_name)
        for player_card in player.cards[cards_index:]:
            print_player_cards(forming_cards(player_card))

            if is_insurance:
                if dealer.get_score() == 21:
                    break
                else:
                    if not is_split and len(player_card) == 2:
                        current_bet -= total_bet / 2
                        print(f"{'':>{int(term_width / 3)}}Lost insurance.\n")

            print_player_info(
                player.get_score(cards_index),
                current_bet,
                player_money
            )

            if surrender:
                if surrender[cards_index]:
                    surrender.remove(surrender[cards_index])
            surrender.append(0)

            # check if player has blackjack on first hand
            if player.get_score() == 21 and len(player_card) == 2:
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
                        player_money += total_bet
                        stop_game = True
                        break
                elif dealer.get_score() < 10:
                    player_money += total_bet * 1.5
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
                    len(dealer.cards[0]),
                    player_money,
                    current_bet,
                    is_double_down,
                    is_split,
                    is_insurance
                )

                # output actions list
                print()
                for number, action in enumerate(actions, start=1):
                    print(f"{'':>{int(term_width / 3)}}{number}. {action}")

                action = choose_action(len(actions))

                if actions[action - 1] == 'Hit':
                    player.hit(deck.get_card(), cards_index)
                    cards_index -= 1
                    break
                elif actions[action - 1] == 'Surrender':
                    player_money += total_bet / 2
                    current_bet -= total_bet / 2
                    surrender.remove(surrender[cards_index])
                    surrender.insert(cards_index, 1)
                    break
                elif actions[action - 1] == 'Double down':
                    # player can choice double down one time per game
                    is_double_down = True
                    player.hit(deck.get_card(), cards_index)
                    player_money -= total_bet
                    current_bet += total_bet
                    cards_index -= 1
                    break
                elif actions[action - 1] == 'Insurance':
                    # player can choice insurance one time per game
                    is_insurance = True
                    player_money -= total_bet / 2
                    current_bet += total_bet / 2
                    dealer.hit(deck.get_card())
                    cards_index -= 1
                    break
                elif actions[action - 1] == 'Split':
                    is_split = True
                    split_cards: List = [
                        [player_card[1], *deck.get_card()],
                        [player_card[0], *deck.get_card()]
                    ]

                    player.cards.remove(player.cards[cards_index])
                    for split_card in split_cards:
                        player.cards.insert(cards_index, split_card)

                    surrender.remove(surrender[cards_index])
                    for i in range(2):
                        surrender.append(0)

                    player_money -= total_bet
                    current_bet += total_bet

                    # if was split two Aces
                    if split_cards[0][0][0] == 11:
                        cards_index += 1
                    else:
                        cards_index -= 1
                    break
                else:
                    break
        cards_index += 1

    if not blackjack and not stop_game:
        if len(surrender) == 1 and surrender[0] != 1 or len(surrender) > 1:
            # dealer must taking cards until 17 score
            while dealer.get_score() < 17:
                dealer.hit(deck.get_card())

    clear_terminal()
    print()

    # print final dealer and player card
    player_title(dealer.get_name)
    for dealer_card in dealer.cards:
        print_player_cards(forming_cards(dealer_card))
    print(f"{'':>{int(term_width / 3)}}Score: {dealer.get_score()}")

    if not is_split:
        player_title(player.get_name)
        for card in player.cards:
            print_player_cards(forming_cards(card))

        print_player_info(
            player.get_score(0),
            current_bet,
            player_money
        )
    else:
        player_title(player.get_name)
        print(f"{'':>{int(term_width / 3)}}"
              f"{player.get_name.title()}"
              f" score list: {player.get_score_list}")

    separator()
    # result of the game
    if blackjack or stop_game:
        if blackjack:
            print(f"{'':>{int(term_width / 3)}}{player.get_name.title()} "
                  f"win! Blackjack!\n")
        if stop_game:
            print(f"{'':>{int(term_width / 3)}}{player.get_name.title()} "
                  f"stopped the game and took the bet back.")
    else:
        for index in range(len(player.get_score_list)):
            if player.get_score(index) > 21 < dealer.get_score() \
                    or 21 > player.get_score(index) == dealer.get_score() \
                    or player.get_score(index) == 21 == dealer.get_score():
                push += 1
                if is_double_down:
                    player_money += total_bet * 2
                else:
                    player_money += total_bet

            elif player.get_score(index) < 21 < dealer.get_score() \
                    or player.get_score(index) == 21 < dealer.get_score() \
                    or player.get_score(index) == 21 > dealer.get_score() \
                    or 21 > player.get_score(index) > dealer.get_score():
                if not surrender[index]:
                    win += 1
                    if is_double_down:
                        player_money += (total_bet * 2) * 1.5
                    else:
                        player_money += total_bet * 1.5
                else:
                    lose += 1
            else:
                if dealer.get_score() == 21 != player.get_score(index) \
                        and len(dealer.cards[0]) == 2 and is_insurance:
                    player_money += total_bet
                    print(f"{'':>{int(term_width / 3)}}"
                          f"{player.get_name.title()} "
                          f"received insurance.\n")
                lose += 1

    # show the game result
    if len(player.get_score_list) > 1:
        print(f"{'':>{int(term_width / 3)}}Push: {push} pair of cards.")
        print(f"{'':>{int(term_width / 3)}}Win: {win} pair of cards.")
        print(f"{'':>{int(term_width / 3)}}Lose: {lose} pair of cards.\n")
    else:
        if surrender[0]:
            print(f"{'':>{int(term_width / 3)}}{player.get_name.title()} "
                  f"surrendered.")
        else:
            if push:
                print(f"{'':>{int(term_width / 3)}}Push.\n")
            if win:
                print(f"{'':>{int(term_width / 3)}}"
                      f"{player.get_name.title()} won!\n")
            if lose:
                print(f"{'':>{int(term_width / 3)}}"
                      f"{dealer.get_name.title()} won.\n")

    print(
        f"{'':>{int(term_width / 3)}}{player.get_name.title()}'s money: "
        f"{player_money}"
    )

    if player_money and is_continue('Continue the game'):
        # set default values if continue the game
        del player.cards
        del dealer.cards
        cards_index, win, lose, push, total_bet = 0, 0, 0, 0, 0
        is_insurance, is_double_down, is_split = False, False, False
        blackjack, stop_game = False, False
        surrender = []
        continue
    break
