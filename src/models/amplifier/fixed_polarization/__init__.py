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
        Ibq = (self.input.Vcc - 0.7)/self.input.Rb
        Ieq = (self.input.beta + 1)*Ibq

        re = 26e-3/Ieq
        Zi = 1/((1/self.input.Rb) + (1/(self.input.beta*re)))
        Zo = 1/((1/self.input.Rc) + (1/self.input.ro))
        Avnl = -Zo/re
        return Output(re, Zi, Zo, Avnl)

    def draw(self):
        return drawing.draw(self.input)
