from typing import Tuple
from random import sample
from dataclasses import dataclass, field


@dataclass
class Deck:
    _deck: Tuple = field(default_factory=tuple)

    def get_card(self, num: int = 1) -> Tuple[Tuple[int, str, str], ...]:
        """Method return 1 (default) or num cards from deck of cards"""
        return tuple(sample(self._deck, num))
