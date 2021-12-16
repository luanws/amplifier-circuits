from typing import Dict, List, Optional, Type

import numpy as np
from matplotlib import pyplot as plt
from src.models.amplifier import (Amplifier, common_base_polarization_tbj,
                                  common_drain_polarization_fet,
                                  fixed_polarization_fet,
                                  fixed_polarization_tbj,
                                  follower_emitter_polarization_tbj,
                                  voltage_divider_polarization_fet,
                                  voltage_divider_polarization_tbj)


class MainViewModel:
    amplifier_class: Type[Amplifier]
    amplifier: Optional[Amplifier] = None
    amplifiers_dict: Dict[str, Type[Amplifier]] = {
        "Polarização fixa TBJ": fixed_polarization_tbj.Amplifier,
        "Polarização seguidor emissor TBJ": follower_emitter_polarization_tbj.Amplifier,
        "Polarização por divisor de tensão TBJ": voltage_divider_polarization_tbj.Amplifier,
        "Polarização base comum TBJ": common_base_polarization_tbj.Amplifier,
        "Polarização fixa FET": fixed_polarization_fet.Amplifier,
        "Polarização por divisor de tensão FET": voltage_divider_polarization_fet.Amplifier,
        "Polarização dreno comum FET": common_drain_polarization_fet.Amplifier,
    }

    def __init__(self) -> None:
        self.amplifier_class = next(iter(self.amplifiers_dict.values()))

    @property
    def amplifier_names(self) -> List[str]:
        return list(self.amplifiers_dict.keys())

    def set_amplifier_class_by_polarization_name(self, polarization: str) -> None:
        self.amplifier_class = self.amplifiers_dict[polarization]

    def get_amplifier(self, parameters: Dict[str, str]) -> Amplifier:
        for key in parameters.keys():
            parameters[key] = float(parameters[key])
        return self.amplifier_class(**parameters)

    def generate_graphic(self, path: str):
        figure, ax = plt.subplots(2, 1, sharex=True)
        t = np.linspace(0, 25, 1000)
        Vi = np.sin(t)
        Vo = Vi*self.amplifier().Avnl

        ax[0].set_xlabel('t')
        ax[0].set_ylabel('V')
        ax[0].set_title('Vi')
        ax[0].plot(t, Vi, label='Vi', color='r', linewidth=2)
        ax[1].set_title('Vo')
        ax[1].plot(t, Vo, label='Vo', color='g', linewidth=2)
        ax[1].set_xlabel('t')
        ax[1].set_ylabel('V')

        figure.tight_layout(pad=2)
        plt.savefig(path, transparent=True)
