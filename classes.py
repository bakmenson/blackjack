from random import choice
from typing import Tuple, List


class DeckOfCards:
    def __init__(self, cards: Tuple, symbols: Tuple) -> None:
        self.card: Tuple[str, int] = choice([_ for _ in cards])
        self.symbol: str = choice([_ for _ in symbols])

    def get_card(self):
        return (
            f"{chr(9484)}{chr(9472) * 9}{chr(9488)}",
            f"{chr(9474)}\033[0;30;47m{self.card[0]:<2}"
            + f"\033[0m\033[0;30;47m \033[0m" * 7 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 9 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 9 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 4 + f"{self.symbol}"
            + f"\033[0;30;47m \033[0m" * 4 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 9 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 9 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 7
            + f"\033[0;30;47m{self.card[0]:>2}\033[0m{chr(9474)}",
            f"{chr(9492)}{chr(9472) * 9}{chr(9496)}"
        )

    def get_card_value(self):
        return self.card[1]


class Player:
    def __init__(self, cards_lst: List) -> None:
        self.card_lst: List[Tuple[str]]

        if len(cards_lst) == 1:
            self.card_lst = [_ for _ in zip(cards_lst[0].get_card())]
        else:
            self.card_lst = [_ for _ in zip(cards_lst[0].get_card(),
                                            cards_lst[1].get_card())]
