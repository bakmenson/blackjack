from typing import Tuple, List, Union, Optional, Any
from dataclasses import dataclass, field


@dataclass
class Player:
    _name: str = 'unknown player'
    _cards: List = field(default_factory=list)

    def __len__(self):
        return len(self._cards)

    @property
    def cards(self) -> Union[
        List[Tuple[int, str, str]],
        List[List[Tuple[int, str, str]]],
        List[Any]
    ]:
        """Method returns player cards"""
        return self._cards

    @cards.setter
    def cards(
            self,
            cards: Union[List[Tuple[int, str, str]], List[Any]]
    ) -> None:
        """Method gives player cards for start new game"""
        if len(cards) == 1:
            self._cards: List[Tuple[int, str, str]] = cards
        else:
            self._cards: List[List[Tuple[int, str, str]]] = [cards]

    @cards.deleter
    def cards(self) -> None:
        self._cards = []

    def hit(
            self,
            card: List[Tuple[int, str, str]],
            card_index: Optional[int] = None
    ) -> None:
        """Method hit (adds) card into player cards"""
        if card_index is None:
            self._cards.extend(card)
        else:
            self._cards[card_index].extend(card)

    def get_score(self, card_index: Optional[int] = None) -> int:
        """Method returns player scores"""
        if card_index is None:
            return sum(num[0] for num in self._cards)
        return sum(num[0] for num in self._cards[card_index])

    @property
    def get_name(self) -> str:
        """Method returns player name"""
        return self._name


class HumanPlayer(Player):
    def split_cards(
            self,
            card_index: int,
            card: List[List[Union[int, str, str]]]
    ) -> None:
        """Method splits player cards"""
        # adding new cards instead of splitted card
        self._cards[card_index] = card
        # unpacking new cards in player cards list
        self._cards = [y for x in self._cards for y in x]
