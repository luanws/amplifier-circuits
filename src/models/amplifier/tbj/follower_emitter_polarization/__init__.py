import math

from src.models.amplifier import Amplifier as _Amplifier

from . import drawing
from .input import Input
from .output import Output


class Amplifier(_Amplifier):
    input: Input = Input(*[0 for _ in Input.get_parameter_names()])
    output: Output = Output(*[0 for _ in Output.get_parameter_names()])

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self.input = Input(*args, **kwargs)

    def __call__(self) -> Output:
        Vcc = self.input.Vcc
        Rb = self.input.Rb
        Re = self.input.Re
        beta = self.input.beta
        ro = self.input.ro
        Rs = self.input.Rs
        Rl = self.input.Rl
        Ci = self.input.Ci
        Co = self.input.Co
        Ce = self.input.Ce
        Cwi = self.input.Cwi
        Cwo = self.input.Cwo
        Cce = self.input.Cce
        Cbe = self.input.Cbe
        Cbc = self.input.Cbc

        Ibq = (Vcc - 0.7)/(Rb + Re*(beta + 1))
        Ieq = (beta + 1)*Ibq

        re = 26e-3/Ieq
        Zb = beta*(Re + re)
        Zi = 1/((1/Rb) + (1/Zb))
        Zo = 1/((1/(beta*re)) + (1/Re) + (1/ro) + (1/re))
        Avnl = Re/(Re + re)

        Avl = Avnl*(Rl/(Rl + Zo))

        Cmi = Cbc*(1 - Avl)
        Chi = Cwi + Cbe + Cmi
        Cmo = Cbc*(1 - 1/Avl)
        Cho = Cwo + Cce + Cmo

        Fli = 1/(2*math.pi*Ci*(Zi + Rs))
        Flo = 1/(2*math.pi*Co*(Zo + Rl))

        Fhi = 1/(2*math.pi*Chi*(1/(1/Rs + 1/Zi)))
        Fho = 1/(2*math.pi*Cho*(1/(1/Rl + 1/Zo)))
        Ft = 1/(2*math.pi*re*(Cbe + Cbc))

        Fh = min(Fhi, Fho, Ft)
        Fl = max(Fli, Flo)

        Av = Avnl*(Zi/(Zi + Rs))*(Rl/(Rl + Zo))

        return Output(re, Zi, Zo, Avnl, Av, Fl, Fh)

    @staticmethod
    def draw_void():
        return drawing.draw_void()

    def draw(self):
        return drawing.draw(self.input)
