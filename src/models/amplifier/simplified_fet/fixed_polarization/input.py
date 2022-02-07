from src.models.amplifier.input import Input as _Input


class Input(_Input):
    Vdd: float
    Vgg: float
    Vp: float
    Idss: float
    rd: float
    Rd: float
    Rg: float

    def __init__(self, Vdd: float, Vgg: float, Vp: float, Idss: float, rd: float, Rd: float, Rg: float):
        self.Vdd = Vdd
        self.Vgg = Vgg
        self.Vp = Vp
        self.Idss = Idss
        self.rd = rd
        self.Rd = Rd
        self.Rg = Rg

    @staticmethod
    def get_parameter_names() -> list[str]:
        return ['Vdd', 'Vgg', 'Vp', 'Idss', 'rd', 'Rd', 'Rg']

    @staticmethod
    def get_parameter_units() -> list[str]:
        return ['V', 'V', 'V', 'A', 'Ω', 'Ω', 'Ω']
