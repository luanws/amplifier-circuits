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
        beta = self.input.beta
        ro = self.input.ro
        R1 = self.input.R1
        R2 = self.input.R2
        Rc = self.input.Rc
        Re = self.input.Re
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

        R_line = 1/((1/R1) + (1/R2))
        Vb = Vcc*R2/(R1 + R2)
        Vbe = 0.7
        Ve = Vb - Vbe
        Ieq = Ve/Re

        Zo = 1/((1/ro) + (1/Rc))
        re = 26e-3/Ieq
        Zi = 1/((1/R_line) + (1/(beta*re)))
        Avnl = -Zo/re

        Avl = Avnl*(Rl/(Rl + Zo))

        Cmi = Cbc*(1 - Avl)
        Chi = Cwi + Cbe + Cmi
        Cmo = Cbc*(1 - 1/Avl)
        Cho = Cwo + Cce + Cmo

        Ri = 1/(1/R1 + 1/R2 + 1/Rs)
        Zeq = 1/(1/Re + 1/(Ri/beta + re))

        Fli = 1/(2*math.pi*Ci*(Zi + Rs))
        Flo = 1/(2*math.pi*Co*(Zo + Rl))
        Fle = 1/(2*math.pi*Ce*Zeq)

        Fhi = 1/(2*math.pi*Chi*(1/(1/Rs + 1/Zi)))
        Fho = 1/(2*math.pi*Cho*(1/(1/Rl + 1/Zo)))
        Ft = 1/(2*math.pi*re*(Cbe + Cbc))

        Fh = min(Fhi, Fho, Ft)
        Fl = max(Fli, Flo, Fle)

        Av = Avnl*(Zi/(Zi + Rs))*(Rl/(Rl + Zo))

        return Output(re, Zi, Zo, Avnl, Av, Fl, Fh)

    @staticmethod
    def draw_void():
        return drawing.draw_void()

    def draw(self):
        return drawing.draw(self.input)
