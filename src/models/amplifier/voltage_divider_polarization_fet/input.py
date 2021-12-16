from typing import List

from src.models.amplifier.input import Input as _Input


class Input(_Input):
    Vdd: float
    R1: float
    R2: float
    Rd: float
    Rs: float
    Vp: float
    Idss: float
    rd: float

    def __init__(self, Vdd: float, R1: float, R2: float, Rd: float, Rs: float, Vp: float, Idss: float, rd: float) -> None:
        self.Vdd = Vdd
        self.R1 = R1
        self.R2 = R2
        self.Rd = Rd
        self.Rs = Rs
        self.Vp = Vp
        self.Idss = Idss
        self.rd = rd

    @staticmethod
    def get_parameter_names() -> List[str]:
        return ['Vdd', 'R1', 'R2', 'Rd', 'Rs', 'Vp', 'Idss', 'rd']
