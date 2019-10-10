from typing import Tuple
from dataclasses import dataclass, field


@dataclass
class Player:
    _name: str = 'unknown player'
    _cards: Tuple[Tuple[int, str, str], ...] = field(default_factory=tuple)

    def add_card(self, card: Tuple[Tuple[int, str, str], ...]) -> \
            Tuple[Tuple[int, str, str], ...]:
        self._cards += (*card,)
        return self._cards

    def get_cards(self) -> Tuple[Tuple[int, str, str], ...]:
        return self._cards

    @property
    def get_scores(self) -> int:
        return sum((num[0] for num in self._cards))

    def remove_cards(self) -> Tuple:
        self._cards = tuple()
        return self._cards

    def get_name(self) -> str:
        return self._name
