from src.models.amplifier.output import Output as _Output


class Output(_Output):
    re: float
    Zi: float
    Zo: float
    Avnl: float
    Av: float
    Fl: float
    Fh: float

    def __init__(
        self, re: float, Zi: float, Zo: float,
        Avnl: float, Av: float, Fl: float, Fh: float
    ) -> None:
        self.re = re
        self.Zi = Zi
        self.Zo = Zo
        self.Avnl = Avnl
        self.Av = Av
        self.Fl = Fl
        self.Fh = Fh

    def __str__(self) -> str:
        return '\n'.join([
            f"re = {self.re:.2f} Ω",
            f"Zi = {self.Zi:.2f} Ω",
            f"Zo = {self.Zo:.2f} Ω",
            f"Avnl = {self.Avnl:.2f}",
            f"Av = {self.Av:.2f}",
            f"Fl = {self.Fl:.2f} Hz",
            f"Fh = {self.Fh:.2f} Hz"
        ])

    def __repr__(self) -> str:
        return self.__str__()

    @ staticmethod
    def get_parameter_names() -> list[str]:
        return ['re', 'Zi', 'Zo', 'Avnl', 'Av', 'Fl', 'Fh']

    @ staticmethod
    def get_parameter_units() -> list[str]:
        return ['Ω', 'Ω', 'Ω', '', '', 'Hz', 'Hz']
