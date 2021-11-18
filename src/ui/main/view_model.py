from typing import Dict, List

from src.models.amplifier import (Amplifier, fixed_polarization,
                                  follower_emitter_polarization,
                                  voltage_divider_polarization)


class MainViewModel:
    amplifiers_dict: Dict[str, Amplifier] = {
        "Polarização fixa": fixed_polarization.Amplifier,
        "Polarização seguidor emissor": follower_emitter_polarization.Amplifier,
        "Polarização por divisor de tensão": voltage_divider_polarization.Amplifier
    }

    @property
    def amplifier_names(self) -> List[str]:
        return list(self.amplifiers_dict.keys())
