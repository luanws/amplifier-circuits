from typing import List

from src.models.amplifier.output import Output as _Output


class Output(_Output):
    Zi: float
    Zo: float
    Avnl: float

    def __init__(self, Zi: float, Zo: float, Avnl: float) -> None:
        self.Zi = Zi
        self.Zo = Zo
        self.Avnl = Avnl

    def __str__(self) -> str:
        return '\n'.join([
            f"Zi = {self.Zi:.2f} Ω",
            f"Zo = {self.Zo:.2f} Ω",
            f"Avnl = {self.Avnl:.2f}"
        ])

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def get_parameter_names() -> List[str]:
        return ['Zi', 'Zo', 'Avnl']
