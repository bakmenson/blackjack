from typing import Tuple, List
from dataclasses import dataclass, field


@dataclass
class Player:
    _name: str = 'unknown player'
    _cards: List[Tuple[int, str, str]] = field(default_factory=list)

    def add_card(self, card: List[Tuple[int, str, str]]) -> \
            List[Tuple[int, str, str]]:
        self._cards.extend(card)
        return self._cards

    def get_cards(self) -> List[Tuple[int, str, str]]:
        return self._cards

    @property
    def get_scores(self) -> int:
        return sum((num[0] for num in self._cards))

    def remove_cards(self) -> List:
        self._cards = list()
        return self._cards

    @property
    def get_name(self) -> str:
        return self._name
