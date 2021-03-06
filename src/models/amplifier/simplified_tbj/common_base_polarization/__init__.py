from src.models.amplifier import Amplifier as _Amplifier

from . import drawing
from .input import Input
from .output import Output


class Amplifier(_Amplifier):
    input: Input = Input(0, 0, 0, 0, 0, 0)
    output: Output = Output(0, 0, 0, 0)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self.input = Input(*args, **kwargs)

    def __call__(self) -> Output:
        Vcc = self.input.Vcc
        beta = self.input.beta
        ro = self.input.ro
        R1 = self.input.R1
        R2 = self.input.R2
        Re = self.input.Re

        Rb = 1/((1/R1) + (1/R2))
        Vbe = 0.7
        Ibq = (Vcc - Vbe)/(Rb + Re*(beta + 1))
        Ieq = (beta + 1)*Ibq

        re = 26e-3/Ieq
        Zb = beta*(Re + re)
        Zi = 1/((1/Rb) + (1/(Zb)))
        Zo = 1/((1/(beta*ro)) + (1/Re) + (1/ro) + (1/re))
        Avnl = Re/(Re + re)

        return Output(re, Zi, Zo, Avnl)

    @staticmethod
    def draw_void():
        return drawing.draw_void()

    def draw(self):
        return drawing.draw(self.input)
