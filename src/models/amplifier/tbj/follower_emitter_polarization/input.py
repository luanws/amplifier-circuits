from src.models.amplifier.input import Input as _Input


class Input(_Input):
    Vcc: float
    Rb: float
    Re: float
    beta: float
    ro: float

    def __init__(self, Vcc: float, Rb: float, Re: float, beta: float, ro: float):
        self.Vcc = Vcc
        self.Rb = Rb
        self.Re = Re
        self.beta = beta
        self.ro = ro

    @staticmethod
    def get_parameter_names() -> list[str]:
        return ['Vcc', 'beta', 'ro', 'Rb', 'Re']

    @staticmethod
    def get_parameter_units() -> list[str]:
        return ['V', '', 'Ω', 'Ω', 'Ω']
