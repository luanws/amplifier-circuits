from src.models.amplifier import Amplifier as _Amplifier
from src.models.amplifier.output import Output

from . import drawing
from .input import Input


class Amplifier(_Amplifier):
    input: Input

    def __init__(self, amplifier_input: Input) -> None:
        super().__init__()
        self.input = amplifier_input

    def __call__(self) -> Output:
        R_line = 1/((1/self.input.R1) + (1/self.input.R2))
        Vb = self.input.Vcc*self.input.R2/(self.input.R1 + self.input.R2)
        Vbe = 0.7
        Ve = Vb - Vbe
        Ieq = Ve/self.input.Re

        Zo = 1/((1/self.input.ro) + (1/self.input.Rc))
        re = 26e-3/Ieq
        Zi = 1/((1/R_line) + (1/(self.input.beta*re)))
        Avnl = -Zo/re

        return Output(re, Zi, Zo, Avnl)

    def draw(self):
        return drawing.draw(self.input)
