from typing import List, Union
from dataclasses import dataclass
from dealer import Dealer


@dataclass
class Player(Dealer):
    _money: Union[int, float] = 0

    def __len__(self):
        return len(self._cards)

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
