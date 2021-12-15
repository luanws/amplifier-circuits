from typing import List

from src.models.amplifier.input import Input as _Input


class Input(_Input):
    Vcc: float
    Vgg: float
    Vp: float
    Idss: float
    rd: float
    Rd: float
    Rg: float

    def __init__(self, Vcc: float, Vgg: float, Vp: float, Idss: float, rd: float, Rd: float, Rg: float):
        self.Vcc = Vcc
        self.Vgg = Vgg
        self.Vp = Vp
        self.Idss = Idss
        self.rd = rd
        self.Rd = Rd
        self.Rg = Rg

    @staticmethod
    def get_parameter_names() -> List[str]:
        return ['Vcc', 'Vgg', 'Vp', 'Idss', 'rd', 'Rd', 'Rg']
