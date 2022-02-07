from src.models.amplifier.input import Input as _Input


class Input(_Input):
    Vcc: float
    Rc: float
    beta: float
    ro: float
    Rb: float
    Rs: float
    Rl: float
    Ci: float
    Co: float
    Cwi: float
    Cwo: float
    Cce: float
    Cbe: float
    Cbc: float

    def __init__(
        self, Vcc: float, Rc: float, beta: float, ro: float, Rb: float,
        Rs: float, Rl: float, Ci: float, Co: float,
        Cwi: float, Cwo: float, Cce: float, Cbe: float, Cbc: float
    ) -> None:
        self.Vcc = Vcc
        self.Rc = Rc
        self.beta = beta
        self.ro = ro
        self.Rb = Rb
        self.Rs = Rs
        self.Rl = Rl
        self.Ci = Ci
        self.Co = Co
        self.Cwi = Cwi
        self.Cwo = Cwo
        self.Cce = Cce
        self.Cbe = Cbe
        self.Cbc = Cbc

    @staticmethod
    def get_parameter_names() -> list[str]:
        return ['Vcc', 'beta', 'ro', 'Rb', 'Rc', 'Rs', 'Rl', 'Ci', 'Co', 'Cwi', 'Cwo', 'Cce', 'Cbe', 'Cbc']

    @staticmethod
    def get_parameter_units() -> list[str]:
        return ['V', '', 'Ω', 'Ω', 'Ω', 'Ω', 'Ω', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
