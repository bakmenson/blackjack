# from __future__ import annotations
from typing import Any, List, Union
from os import get_terminal_size, system, name

term_width: int = get_terminal_size()[0]


def clear() -> None:
    """Function clear terminal window"""
    system('cls' if name == 'nt' else 'clear')


def separator() -> None:
    """Function print separator"""
    print('\n' + '-' * term_width)


def title(player_name: str) -> None:
    """Function print separator with player title"""
    player_name += ' cards'
    len_title_line: int = (
        (int(term_width / 2) - int((len(player_name) / 2) + 1))
        + (int(term_width / 2) - int((len(player_name) / 2) + 1))
        + len(player_name)
    ) + 2

    end_sep_count: int = 2 if (len_title_line > term_width) else 1 \
        if (len_title_line == term_width) else 0

    print(
        '-' * (int(term_width / 2) - int((len(player_name) / 2) + 1)),
        player_name.title(),
        '-' * (int(term_width / 2) - int((len(player_name) / 2)
                                         + end_sep_count)) + '\n'
    )


def form_cards(player_cards: List) -> List[Any]:
    """Function forms player cards for print() in terminal"""
    cards = tuple((i[1], i[2], i[1]) for i in player_cards)
    result: List = list()
    for n, i in enumerate(cards):
        result.append(
            (f"{chr(9616)}\033[0;30;47m{cards[n][0]:<2}\033[0m"
             + f"{chr(9608)}" * 7 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 4 + f"{cards[n][1]}"
             + f"{chr(9608)}" * 4 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 7
             + f"\033[0;30;47m{cards[n][2]:>2}\033[0m{chr(9612)}"),
        )

    return result


def print_player_cards(cards) -> None:
    """Function prints cards"""
    join_cards = tuple(''.join(i) for i in zip(*cards))
    len_short_str: int = min(len(i) for i in join_cards)
    for card in join_cards:
        align_str: int = (len(card) - len_short_str) \
            if (len(card) > len_short_str) else 0
        print(f"{card:^{term_width + align_str}}")
    print()


def make_bet(
        available_chips: List[Union[int, float], ...]
) -> Union[int, float]:
    """
    Function returns selected chip
    """
    chip_idx: int = 0

    while True:
        try:
            chip_idx = int(
                input(f"\n{'>>> ':>{int(term_width / 3) + 3}}")
            ) - 1
            if chip_idx < 0 or chip_idx > len(available_chips) - 1:
                raise IndexError('Wrong command. Command not found.')
        except ValueError:
            print(f"{'':^{int(term_width / 2) - 16}}"
                  f"Wrong command. Select chip number.")
            continue
        except IndexError as e:
            print(f"{'':^{int(term_width / 2) - 17}}", e)
            continue
        break

    return available_chips[chip_idx]


def input_money() -> int:
    money: int = 0
    input_text = 'Input amount of your money: '
    while True:
        try:
            money = int(input(f"{input_text:>{int(term_width / 2) + 14}}"))
            if money <= 0:
                raise ValueError
        except ValueError:
            print(f"{'':^{int(term_width / 2) - 14}}Invalid amount of money.")
            continue
        break
    return money


def is_continue(question: str) -> bool:
    question += '? (y/n) >>> '
    while True:
        answer = input(f"{'':>{int(term_width / 3)}}{question}")
        if answer != 'y' and answer != 'n':
            print(f"{'':>{int(term_width / 3)}}Wrong command.")
            continue
        break

    return True if answer == 'y' else False


def get_actions(
        player_score: int,
        player_cards: List,
        dealer_score: int,
        dealer_len_cards: int,
        money: Union[int, float],
        bet: Union[int, float],
        double_count: int,
        insurance_count: int
) -> List:
    """Function returns list of the actions."""
    actions_list = ['Hit', 'Stay', 'Surrender']

    if player_score >= 10 and money >= bet * 2 and not double_count:
        actions_list.insert(2, 'Double down')
    if len(player_cards) == 2 and player_cards[0][1] == player_cards[1][1]:
        actions_list.insert(-1, 'Split')
    if dealer_score == 11 and dealer_len_cards == 1 and not insurance_count:
        actions_list.insert(-1, 'Insurance')

    return actions_list


def choose_action(actions: List) -> str:
    """Function returns selected action."""
    action_num: int = 0
    while True:
        try:
            action_num = int(input(f"{'':>{int(term_width / 3)}}>>> "))
            if action_num <= 0 or action_num > len(actions):
                raise IndexError
        except ValueError:
            print(f"{'':>{int(term_width / 3)}}Wrong command.")
            continue
        except IndexError:
            print(f"{'':>{int(term_width / 3)}}Wrong command.")
            continue
        break
    return actions[action_num - 1]


def print_player_info(
        score: int,
        bet: Union[int, float],
        money: Union[int, float],
        insurance: Union[int, float],
) -> None:
    print(f"{'':>{int(term_width / 3)}}Score: {score}")
    print(f"{'':>{int(term_width / 3)}}Bet: {bet}")
    print(f"{'':>{int(term_width / 3)}}Money: {money - insurance}")
    if insurance:
        print(f"{'':>{int(term_width / 3)}}Insurance: {insurance}")
