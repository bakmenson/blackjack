from typing import Tuple, List, Any
from random import sample
from dataclasses import dataclass


@dataclass
class Deck:
    _card_suits = ('\x1b[0;30;47m' + chr(9824) + '\x1b[0m',
                   '\x1b[0;31;47m' + chr(9830) + '\x1b[0m',
                   '\x1b[0;31;47m' + chr(9829) + '\x1b[0m',
                   '\x1b[0;30;47m' + chr(9827) + '\x1b[0m')

    # _card_faces = (*(str(_) for _ in range(2, 11)), 'J', 'Q', 'K', 'A')
    # _card_values = (*(_ for _ in range(2, 10)), *(10 for _ in range(4)), 11)
    _card_faces = ('3',)
    _card_values = (3,)

    def _get_deck(self) -> Tuple[Any, ...]:
        """Method returns deck of cards (4 cards for each suit)"""
        return tuple(
            (*i[0], i[1]) for card in (
                zip((_,) * 4, self._card_suits) for _ in zip(self._card_values,
                                                             self._card_faces)
            )
            for i in card
        )

    def get_card(self, num: int = 1) -> List[Tuple[int, str, str]]:
        """Method return 1 (default) or num cards from deck of cards"""
        return sample(self._get_deck(), num)
