from typing import Tuple
from random import sample
from dataclasses import dataclass, field


@dataclass
class Deck:
    deck: Tuple = field(default_factory=tuple)

    def get_card(self, num: int = 1) -> Tuple[Tuple[int, str, str], ...]:
        """Method return 1 (default) or num cards from deck of cards"""
        return tuple(sample(self.deck, num))


@dataclass
class Player:
    cards: Tuple[Tuple[int, str, str], ...]

    def get_player_cards(self) -> Tuple[Tuple[str, str, str], ...]:
        return tuple((i[1], i[2], i[1]) for i in self.cards)

    @property
    def get_cards_value(self) -> int:
        return sum((num[0] for num in self.cards))

    def add_card(self, card: Tuple[Tuple[int, str, str], ...]) -> None:
        unpacked_card = *card,
        self.cards += unpacked_card
