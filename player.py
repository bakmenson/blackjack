from typing import Tuple
from dataclasses import dataclass, field


@dataclass
class Player:
    name: str = 'unknown player'
    cards: Tuple[Tuple[int, str, str], ...] = field(default_factory=tuple)

    def add_card(self, card: Tuple[Tuple[int, str, str], ...]) -> \
            Tuple[Tuple[int, str, str], ...]:
        self.cards += (*card,)
        return self.cards

    def get_cards(self) -> Tuple[Tuple[int, str, str], ...]:
        return self.cards

    @property
    def get_scores(self) -> int:
        return sum((num[0] for num in self.cards))

    def remove_cards(self) -> Tuple:
        self.cards = tuple()
        return self.cards
