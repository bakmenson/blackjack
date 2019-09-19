from random import choice
from typing import Tuple, List


class DeckOfCards:
    __slots__ = ['card_name', 'card_suit', 'card_value']
    card_name: str
    card_suit: str
    card_value: int

    def __init__(self, cards: Tuple, card_suits: Tuple) -> None:
        self.card_suit = choice([_ for _ in card_suits])
        self.card_name, self.card_value = choice([_ for _ in cards])

    def get_card(self) -> Tuple[str, ...]:
        return (
            f"{chr(9484)}{chr(9472) * 9}{chr(9488)}",
            f"{chr(9474)}\033[0;30;47m{self.card_name:<2}"
            + f"\033[0m\033[0;30;47m \033[0m" * 7 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 9 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 9 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 4 + f"{self.card_suit}"
            + f"\033[0;30;47m \033[0m" * 4 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 9 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 9 + f"{chr(9474)}",
            f"{chr(9474)}" + f"\033[0;30;47m \033[0m" * 7
            + f"\033[0;30;47m{self.card_name:>2}\033[0m{chr(9474)}",
            f"{chr(9492)}{chr(9472) * 9}{chr(9496)}"
        )

    def get_card_value(self) -> int:
        return self.card_value


class Player:
    __slots__ = ['cards_list']

    def __init__(self, cards_list: List) -> None:
        self.cards_list = cards_list

    def get_player_cards(self) -> Tuple[str, ...]:
        return tuple(item.get_card() for item in self.cards_list)

    def get_cards_value(self) -> int:
        return sum((num.get_card_value() for num in self.cards_list))
