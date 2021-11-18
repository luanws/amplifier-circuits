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
        Vcc = self.input.Vcc
        Rb = self.input.Rb
        Re = self.input.Re
        beta = self.input.beta
        ro = self.input.ro

        Ibq = (Vcc - 0.7)/(Rb + Re*(beta + 1))
        Ieq = (beta + 1)*Ibq

        re = 26e-3/Ieq
        Zb = beta*(Re + re)
        Zi = 1/((1/Rb) + (1/Zb))
        Zo = 1/((1/(beta*re)) + (1/Re) + (1/ro) + (1/re))
        Avnl = Re/(Re + re)

        return Output(re, Zi, Zo, Avnl)

    def draw(self):
        return drawing.draw(self.input)
