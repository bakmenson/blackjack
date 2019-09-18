from random import choice
from typing import Tuple, List


class DeckOfCards:
    def __init__(self, cards: Tuple, symbols: Tuple) -> None:
        self.card: Tuple[str, int] = choice([_ for _ in cards])
        self.symbol: str = choice([_ for _ in symbols])

    def get_card(self) -> Tuple[str, ...]:
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

    def get_card_value(self) -> int:
        return self.card[1]


class Player:
    def __init__(self, cards_list: List) -> None:
        self.cards_list = cards_list

    def get_card_lst(self) -> Tuple[str, ...]:
        return tuple(i.get_card() for i in self.cards_list)

    def get_cards_value(self) -> int:
        result = tuple(i.get_card_value() for i in self.cards_list)
        return sum(result)
