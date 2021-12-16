from typing import List

from src.models.amplifier.input import Input as _Input


class Input(_Input):
    Vdd: float
    Rg: float
    Rs: float
    Vp: float
    Idss: float
    rd: float

    def __init__(self, Vdd: float, Rg: float, Rs: float, Vp: float, Idss: float, rd: float):
        self.Vdd = Vdd
        self.Rg = Rg
        self.Rs = Rs
        self.Vp = Vp
        self.Idss = Idss
        self.rd = rd

    @staticmethod
    def get_parameter_names() -> List[str]:
        return ['Vdd', 'Rg', 'Rs', 'Vp', 'Idss', 'rd']
