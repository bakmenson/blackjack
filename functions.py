from __future__ import annotations
from typing import Tuple


def separator(term_width: int) -> None:
    print('\n' + '-' * term_width)


def title(name: str, term_width: int) -> None:
    len_title: int = ((int(term_width / 2) - int((len(name) / 2) + 1))
                      + (int(term_width / 2) - int((len(name) / 2) + 1))
                      + len(name)) + 2

    end_sep_count: int = 2 if (len_title > term_width) else 1 \
        if (len_title == term_width) else 0

    print('-' * (int(term_width / 2) - int((len(name) / 2) + 1)), name,
          '-' * (int(term_width / 2) - int((len(name) / 2) + end_sep_count)))


def form_cards(player: Player) -> Tuple[Tuple[str, ...]]:
    """Function forms player cards for print() in terminal"""
    cards = tuple()
    for n, i in enumerate(player):
        cards += (
            (f"{chr(9616)}\033[0;30;47m{player[n][0]:<2}\033[0m"
             + f"{chr(9608)}" * 7 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 4 + f"{player[n][1]}"
             + f"{chr(9608)}" * 4 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
             f"{chr(9616)}" + f"{chr(9608)}" * 7
             + f"\033[0;30;47m{player[n][2]:>2}\033[0m{chr(9612)}"),
        )

    return cards


def print_player_cards(cards, term_width: int) -> None:
    """Function prints cards"""
    join_cards = tuple(''.join(i) for i in zip(*cards))
    len_short_str: int = min(len(i) for i in join_cards)
    for card in join_cards:
        align_str: int = (len(card) - len_short_str) \
            if (len(card) > len_short_str) else 0
        print(f"{card:^{term_width + align_str}}")


def make_bet(chips: Tuple[int, ...], money: int, term_width: int) -> int:
    chip_idx: int = 0
    available_chips: Tuple[int, ...] = tuple(c for c in chips if money >= c)
    available_chips += (money,)

    while True:
        for chip in enumerate(available_chips, start=1):
            if chip[0] == len(available_chips):
                print(f'{chip[0]:>{int(term_width / 3)}}. All-in ({chip[1]})')
                break
            print(f'{chip[0]:>{int(term_width / 3)}}. {chip[1]}')

        try:
            chip_idx = int(input('\n>>> ')) - 1
            if chip_idx < 0 or chip_idx > len(available_chips) - 1:
                raise IndexError
        except ValueError:
            print('Неверная команда. Укажите номер команды.\n')
            continue
        except IndexError:
            print('Неверная команда. Такой команды нет.\n')
            continue
        break

    return available_chips[chip_idx]


def input_money() -> int:
    money: int = 0
    while True:
        try:
            money = int(input('Введите сумму денег: '))
            if money <= 0:
                raise ValueError
        except ValueError:
            print('Неверно указанна сумма денег.')
            continue
        break
    return money


def is_continue(question: str) -> bool:
    while True:
        answer = input(question + '? (y/n)\n>>> ')
        if answer != 'y' and answer != 'n':
            print('Неверно указанна команда.\n')
            continue
        break

    return True if answer == 'y' else False
