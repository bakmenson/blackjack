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
            f"{chr(9616)}\033[0;30;47m{self.card_name:<2}\033[0m"
            + f"{chr(9608)}" * 7 + f"{chr(9612)}",
            f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
            f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
            f"{chr(9616)}" + f"{chr(9608)}" * 4 + f"{self.card_suit}"
            + f"{chr(9608)}" * 4 + f"{chr(9612)}",
            f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
            f"{chr(9616)}" + f"{chr(9608)}" * 9 + f"{chr(9612)}",
            f"{chr(9616)}" + f"{chr(9608)}" * 7
            + f"\033[0;30;47m{self.card_name:>2}\033[0m{chr(9612)}",
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

    def add_card(self, card: DeckOfCards) -> None:
        self.cards_list.append(card)
