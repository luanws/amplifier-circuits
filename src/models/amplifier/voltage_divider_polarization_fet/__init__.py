from src.models.amplifier import Amplifier as _Amplifier

from . import drawing
from .input import Input
from .output import Output


class Amplifier(_Amplifier):
    input: Input = Input(0, 0, 0, 0, 0, 0, 0, 0)
    output: Output = Output(0, 0, 0, 0)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self.input = Input(*args, **kwargs)

    def __call__(self) -> Output:
        Vdd = self.input.Vdd
        R1 = self.input.R1
        R2 = self.input.R2
        Rd = self.input.Rd
        Rs = self.input.Rs
        Vp = self.input.Vp
        Idss = self.input.Idss
        rd = self.input.rd

        Vgsq = Vdd
        gm = (2*Idss/abs(Vp))*(1 - (Vgsq/Vp))

        Zi = 1/(1/R1 + 1/R2)
        Zo = 1/((1/rd) + (1/Rd))
        Avnl = -gm*Zo
        return Output(gm, Zi, Zo, Avnl)

    @staticmethod
    def draw_void():
        return drawing.draw_void()

    def draw(self):
        return drawing.draw(self.input)
