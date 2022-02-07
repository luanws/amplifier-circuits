from src.models.amplifier.input import Input as _Input


class Input(_Input):
    Vcc: float
    R1: float
    R2: float
    Rc: float
    Re: float
    beta: float
    ro: float
    Rs: float
    Rl: float
    Ci: float
    Co: float
    Ce: float
    Cwi: float
    Cwo: float
    Cce: float
    Cbe: float
    Cbc: float

    def __init__(
        self, Vcc: float, R1: float, R2: float, Rc: float,
        Re: float, beta: float, ro: float, Rs: float,
        Rl: float, Ci: float, Co: float, Ce: float,
        Cwi: float, Cwo: float, Cce: float, Cbe: float, Cbc: float
    ):
        super().__init__()
        self.Vcc = Vcc
        self.R1 = R1
        self.R2 = R2
        self.Rc = Rc
        self.Re = Re
        self.beta = beta
        self.ro = ro
        self.Rs = Rs
        self.Rl = Rl
        self.Ci = Ci
        self.Co = Co
        self.Ce = Ce
        self.Cwi = Cwi
        self.Cwo = Cwo
        self.Cce = Cce
        self.Cbe = Cbe
        self.Cbc = Cbc

    @ staticmethod
    def get_parameter_names() -> list[str]:
        return [
            'Vcc', 'beta', 'ro', 'R1', 'R2', 'Rc',
            'Re', 'Rs', 'Rl', 'Ci', 'Co', 'Ce',
            'Cwi', 'Cwo', 'Cce', 'Cbe', 'Cbc'
        ]

    @ staticmethod
    def get_parameter_units() -> list[str]:
        return [
            'V', '', 'Ω', 'Ω', 'Ω', 'Ω',
            'Ω', 'Ω', 'Ω', 'F', 'F', 'F',
            'F', 'F', 'F', 'F', 'F'
        ]
