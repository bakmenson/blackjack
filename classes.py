from typing import Tuple
from random import sample
from dataclasses import dataclass, field


@dataclass
class Deck:
    cards: Tuple = field(default_factory=tuple())

    def get_card(self, num: int = 1) -> Tuple[Tuple[str, int, str], ...]:
        return tuple(sample(self.cards, num))


@dataclass
class Player:
    cards: Deck.get_card

    def get_player_cards(self) -> Tuple[Tuple[str, int, str], ...]:
        return self.cards

    def get_cards_value(self) -> int:
        return sum((num[0] for num in self.cards))

    def add_card(self, card: Tuple[Tuple[str, int, str], ...]) -> None:
        self.cards += (*card),
