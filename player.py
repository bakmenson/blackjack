from typing import Tuple, List
from dataclasses import dataclass, field


@dataclass
class Player:
    _name: str = 'unknown player'
    _cards: List[Tuple[int, str, str]] = field(default_factory=list)

    def add_card(self, card: List[Tuple[int, str, str]]) -> None:
        """Method add card into player cards"""
        self._cards.extend(card)

    def get_cards(self) -> List[Tuple[int, str, str]]:
        """Method returns player cards"""
        return self._cards

    def get_score(self, card) -> int:
        """Method returns player scores"""
        return sum((num[0] for num in self._cards[card]))

    def remove_card(self, card) -> None:
        """Method remove card from player cards"""
        self._cards.remove(card)

    def remove_cards(self) -> None:
        """Method remove all player cards"""
        self._cards = list()

    def insert_card(self, index, card) -> None:
        """Method insert card in player cards into index position"""
        self._cards.insert(index, card)

    @property
    def get_name(self) -> str:
        """Method returns player name"""
        return self._name
