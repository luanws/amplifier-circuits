from src.models.amplifier.input import Input as _Input


class Input(_Input):
    Vdd: float
    Rg: float
    Rs: float
    Vp: float
    Idss: float
    rd: float
    Idq: float

    def __init__(self, Vdd: float, Rg: float, Rs: float, Vp: float, Idss: float, rd: float, Idq: float):
        self.Vdd = Vdd
        self.Rg = Rg
        self.Rs = Rs
        self.Vp = Vp
        self.Idss = Idss
        self.rd = rd
        self.Idq = Idq

    @staticmethod
    def get_parameter_names() -> list[str]:
        return ['Vdd', 'Vp', 'Idss', 'rd', 'Rg', 'Rs', 'Idq']

    @staticmethod
    def get_parameter_units() -> list[str]:
        return ['V', 'V', 'A', 'Ω', 'Ω', 'Ω', 'A']
