from __future__ import annotations
from os import get_terminal_size


def title(name: str) -> None:
    end_sep: int
    term_width: int = get_terminal_size()[0]
    len_title: int = ((int(term_width / 2) - int((len(name) / 2) + 1))
                      + (int(term_width / 2) - int((len(name) / 2) + 1))
                      + len(name)) + 2

    end_sep = 0
    if len_title > term_width:
        end_sep = 2
    if len_title == term_width:
        end_sep = 1
    print('-' * (int(term_width / 2) - int((len(name) / 2) + 1)), name,
          '-' * (int(term_width / 2) - int((len(name) / 2) + end_sep)))


def print_player_cards(player: Player) -> None:
    for card in zip(*player.get_player_cards()):
        print(*card)


def add_card(player):
    pass
