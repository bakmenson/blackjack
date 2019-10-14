from typing import Tuple, List
from random import sample
from dataclasses import dataclass, field


@dataclass
class Deck:
    _deck: Tuple = field(default_factory=tuple)

    def get_card(self, num: int = 1) -> List[Tuple[int, str, str]]:
        """Method return 1 (default) or num cards from deck of cards"""
        return sample(self._deck, num)
