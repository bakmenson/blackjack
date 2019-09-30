from random import choice
from typing import Tuple, List


class Card:
    __slots__ = ['card_name', 'card_suit', 'card_value']

    def __init__(self, face_cards: Tuple, card_suits: Tuple) -> None:
        self.card_suit: str = choice([_ for _ in card_suits])
        self.card_name: str = choice([_[0] for _ in face_cards])
        self.card_value: int = choice([_[1] for _ in face_cards])

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

    def add_card(self, card: Card) -> None:
        self.cards_list.append(card)
