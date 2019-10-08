from typing import Tuple
from dataclasses import dataclass


@dataclass
class Player:
    cards: Tuple[Tuple[int, str, str], ...]

    def get_cards(self) -> Tuple[Tuple[int, str, str], ...]:
        return self.cards

    @property
    def get_scores(self) -> int:
        return sum((num[0] for num in self.cards))

    def add_card(self, card: Tuple[Tuple[int, str, str], ...]) -> \
            Tuple[Tuple[int, str, str], ...]:
        self.cards += (*card,)
        return self.cards

    def remove_cards(self) -> Tuple:
        self.cards = tuple()
        return self.cards
