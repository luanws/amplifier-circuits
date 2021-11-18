from typing import Dict, List, Type

from src.models.amplifier import (Amplifier, fixed_polarization,
                                  follower_emitter_polarization,
                                  voltage_divider_polarization)


class MainViewModel:
    amplifier_class: Type[Amplifier]
    amplifiers_dict: Dict[str, Type[Amplifier]] = {
        "Polarização fixa": fixed_polarization.Amplifier,
        "Polarização seguidor emissor": follower_emitter_polarization.Amplifier,
        "Polarização por divisor de tensão": voltage_divider_polarization.Amplifier
    }

    def __init__(self) -> None:
        self.amplifier_class = next(iter(self.amplifiers_dict.values()))
        print(self.amplifier_class)

    @property
    def amplifier_names(self) -> List[str]:
        return list(self.amplifiers_dict.keys())

    def set_amplifier_class_by_polarization_name(self, polarization: str) -> None:
        self.amplifier_class = self.amplifiers_dict[polarization]
