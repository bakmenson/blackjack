from typing import Tuple, List, Union
from dataclasses import dataclass, field


@dataclass
class Player:
    _name: str = 'unknown player'
    _cards: List[Tuple[int, str, str]] = field(default_factory=list)

    def add_card(
            self,
            card: Union[
                List[Tuple[int, str, str]], List[List[Tuple[int, str, str]]]
            ],
            idx=None
    ) -> None:
        """Method add card into player cards"""
        if idx is None:
            self._cards.extend(card)
        if idx is not None:
            self._cards[idx].extend(card)

    def get_cards(self) -> List[Tuple[int, str, str]]:
        """Method returns player cards"""
        return self._cards

    def get_score(self, card_index: int = 0):
        """Method returns player scores"""
        return sum(num[0] for num in self._cards[card_index])

    @property
    def get_name(self) -> str:
        """Method returns player name"""
        return self._name
