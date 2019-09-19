from __future__ import annotations
from os import get_terminal_size
from typing import Tuple


def title(name: str) -> None:
    term_width: int = get_terminal_size()[0]
    len_title: int = ((int(term_width / 2) - int((len(name) / 2) + 1))
                      + (int(term_width / 2) - int((len(name) / 2) + 1))
                      + len(name)) + 2

    end_sep_count: int = 2 if len_title > term_width else 1 \
        if len_title == term_width else 0

    print('-' * (int(term_width / 2) - int((len(name) / 2) + 1)), name,
          '-' * (int(term_width / 2) - int((len(name) / 2) + end_sep_count)))


def print_player_cards(player: Player) -> None:
    for card in zip(*player.get_player_cards()):
        print(*card)


def make_bet(chips: Tuple[int, ...]) -> int:
    print('\n', 'Select a chip and place a bet (1-6).\n')
    for chip in enumerate(chips, start=1):
        print(f'{chip[0]:>5}. {chip[1]}')
    chip_idx = int(input('\n>>> ')) - 1
    return chips[chip_idx]
