from typing import Dict, List, Type

from src.models.amplifier import (Amplifier, fixed_polarization,
                                  follower_emitter_polarization,
                                  voltage_divider_polarization)
from src.models.amplifier.input import Input


class MainViewModel:
    amplifier_class: Type[Amplifier]
    amplifiers_dict: Dict[str, Type[Amplifier]] = {
        "Polarização fixa": fixed_polarization.Amplifier,
        "Polarização seguidor emissor": follower_emitter_polarization.Amplifier,
        "Polarização por divisor de tensão": voltage_divider_polarization.Amplifier
    }

    def __init__(self) -> None:
        self.amplifier_class = next(iter(self.amplifiers_dict.values()))

    @property
    def amplifier_names(self) -> List[str]:
        return list(self.amplifiers_dict.keys())

    def set_amplifier_class_by_polarization_name(self, polarization: str) -> None:
        self.amplifier_class = self.amplifiers_dict[polarization]

    def calculate(self, parameters: Dict[str, str]) -> Input:
        for key in parameters.keys():
            parameters[key] = float(parameters[key])
        return self.amplifier_class(**parameters)()
