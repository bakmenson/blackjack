from typing import Tuple, List, Union, Any
from dataclasses import dataclass, field


@dataclass
class BasePlayer:
    _name: str = 'unknown player'
    _cards: List = field(default_factory=list)

    def __len__(self):
        return len(self._cards[0])

    @property
    def cards(self) -> Union[
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
        self._cards: List[List[Tuple[int, str, str]]] = [cards]

    @cards.deleter
    def cards(self) -> None:
        """Method remove all cards"""
        self._cards = []

    def hit(
            self,
            card: List[Tuple[int, str, str]],
            card_index: int = 0
    ) -> None:
        """Method hit (adds) card into player cards"""
        self._cards[card_index].extend(card)

    def get_score(self, card_index: int = 0) -> int:
        """Method returns player score"""
        return self.get_score_list[card_index]

    @property
    def get_score_list(self) -> List[int]:
        """Method returns player scores in list."""

        result, values = [], []
        for i in range(len(self._cards)):
            for value in self._cards[i]:
                values.append(value[0])
            if sum(values) > 21:
                for num in range(len(values)):
                    if values[num] == 11:
                        values[num] = 1
            result.append(sum(values))
            values = []
        return result

    @property
    def get_name(self) -> str:
        """Method returns player name"""
        return self._name


@dataclass
class Player(BasePlayer):
    _money: Union[int, float] = 0

    @property
    def money(self) -> Union[int, float]:
        return self._money

    @money.setter
    def money(self, value: Union[int, float]) -> None:
        self._money = value

    def split_cards(
            self,
            card_index: int,
            split_cards: List[List[Union[int, str, str]]]
    ) -> None:
        """Method splits player cards"""
        self._cards.remove(self._cards[card_index])
        for card in split_cards:
            self._cards.insert(card_index, card)
