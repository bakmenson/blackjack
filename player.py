from typing import Tuple, List, Union, Optional
from dataclasses import dataclass, field


@dataclass
class Player:
    _name: str = 'unknown player'
    _cards: List = field(default_factory=list)

    def set_cards(self, cards: List[Tuple[int, str, str]]) -> None:
        """Method gives player cards in start of the game"""
        if len(cards) == 2:
            self._cards: List[List[Tuple[int, str, str]]] = [cards]
        else:
            self._cards: List[Tuple[int, str, str]] = cards

    def hit(
        self,
        card: List[Tuple[int, str, str]],
        idx=None
    ) -> None:
        """Method hit (adds) card into player cards"""
        if idx is None:
            self._cards.extend(card)
        if idx is not None:
            self._cards[idx].extend(card)

    @property
    def get_cards(self) -> Union[
        List[Tuple[int, str, str]],
        List[List[Tuple[int, str, str]]]
    ]:
        """Method returns player cards"""
        return self._cards

    def get_score(self, card_index: Optional[int] = None) -> int:
        """Method returns player scores"""
        if card_index is None:
            return sum(num[0] for num in self._cards)
        return sum(num[0] for num in self._cards[card_index])

    @property
    def get_name(self) -> str:
        """Method returns player name"""
        return self._name

    def remove_card(self, card: List[Tuple[int, str, str]]) -> None:
        self._cards.remove(card)
