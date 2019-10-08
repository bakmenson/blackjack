from __future__ import annotations
from typing import Tuple, Any, List, Union


def separator(term_width: int) -> None:
    print('\n' + '-' * term_width)


def title(name: str, term_width: int) -> None:
    len_title: int = ((int(term_width / 2) - int((len(name) / 2) + 1))
                      + (int(term_width / 2) - int((len(name) / 2) + 1))
                      + len(name)) + 2

    end_sep_count: int = 2 if (len_title > term_width) else 1 \
        if (len_title == term_width) else 0

    print('-' * (int(term_width / 2) - int((len(name) / 2) + 1)), name,
          '-' * (int(term_width / 2) - int((len(name) / 2) + end_sep_count))
          + '\n')


def form_cards(player_cards: Tuple) -> Tuple[Any, ...]:
    """Function forms player cards for print() in terminal"""
    cards = tuple((i[1], i[2], i[1]) for i in player_cards)
    result: Tuple = tuple()
    for n, i in enumerate(cards):
        result += (
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


def print_player_cards(cards, term_width: int) -> None:
    """Function prints cards"""
    join_cards = tuple(''.join(i) for i in zip(*cards))
    len_short_str: int = min(len(i) for i in join_cards)
    for card in join_cards:
        align_str: int = (len(card) - len_short_str) \
            if (len(card) > len_short_str) else 0
        print(f"{card:^{term_width + align_str}}")
    print()


def make_bet(
        available_chips: Tuple[Union[int, float], ...],
        term_width: int
) -> Union[int, float]:
    """
    Function returns selected chip
    """
    chip_idx: int = 0

    while True:
        try:
            chip_idx = int(input(f"\n{'>>>':>{int(term_width / 3) + 3}} ")) - 1
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


def input_money(term_width: int) -> int:
    money: int = 0
    while True:
        try:
            money = int(input(
                f"{'Input amount of your money: ':>{int(term_width / 2) + 14}}"
            ))
            if money <= 0:
                raise ValueError
        except ValueError:
            print(f"{'':^{int(term_width / 2) - 14}}"
                  f"Invalid amount of money.")
            continue
        break
    return money


def is_continue(question: str, term_width: int) -> bool:
    question += '? (y/n) >>> '
    while True:
        answer = input(f"{'':>{int(term_width / 3)}}{question}")
        if answer != 'y' and answer != 'n':
            print(f"{'':>{int(term_width / 3)}}Wrong command.")
            continue
        break

    return True if answer == 'y' else False


def get_actions(
        score: int,
        cards: Tuple,
        money: Union[int, float],
        bet: Union[int, float],
        double_count: int
) -> List:
    """Function returns list of the actions."""
    split = True if (len(cards) == 2) and (cards[0][1] == cards[1][1]) \
        else False

    actions_list = ['Hit', 'Stay', 'Surrender']

    if score >= 10 and money >= bet * 2 and not double_count:
        actions_list.insert(2, 'Double down')
    if split:
        actions_list.insert(-1, 'Split')

    return actions_list


def choose_action(actions: List, term_width: int) -> str:
    """Function returns the number of the selected action."""
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
