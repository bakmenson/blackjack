from typing import Tuple
from dataclasses import dataclass, field


@dataclass
class Player:
    cards: Tuple[Tuple[int, str, str], ...]

    def get_player_cards(self) -> Tuple[Tuple[str, str, str], ...]:
        return tuple((i[1], i[2], i[1]) for i in self.cards)

    @property
    def get_cards_value(self) -> int:
        return sum((num[0] for num in self.cards))

    def add_card(self, card: Tuple[Tuple[int, str, str], ...]) -> None:
        self.cards += (*card,)
