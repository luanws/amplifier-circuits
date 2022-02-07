from typing import Type

import numpy as np
from matplotlib import pyplot as plt
from src.models.amplifier import Amplifier, simplified_fet, simplified_tbj


class MainViewModel:
    amplifier_class: Type[Amplifier]
    amplifier: Amplifier | None = None
    amplifiers_dict: dict[str, Type[Amplifier]] = {
        "Polarização fixa TBJ (NL)": simplified_tbj.fixed_polarization.Amplifier,
        "Polarização seguidor emissor TBJ (NL)": simplified_tbj.follower_emitter_polarization.Amplifier,
        "Polarização por divisor de tensão TBJ (NL)": simplified_tbj.voltage_divider_polarization.Amplifier,
        "Polarização base comum TBJ (NL)": simplified_tbj.common_base_polarization.Amplifier,
        "Polarização fixa FET (NL)": simplified_fet.fixed_polarization.Amplifier,
        "Polarização por divisor de tensão FET (NL)": simplified_fet.voltage_divider_polarization.Amplifier,
        "Polarização dreno comum FET (NL)": simplified_fet.common_drain_polarization.Amplifier,
    }

    def __init__(self) -> None:
        self.amplifier_class = next(iter(self.amplifiers_dict.values()))

    @property
    def amplifier_names(self) -> list[str]:
        return list(self.amplifiers_dict.keys())

    def set_amplifier_class_by_polarization_name(self, polarization: str) -> None:
        self.amplifier_class = self.amplifiers_dict[polarization]

    def get_amplifier(self, parameters: dict[str, float]) -> Amplifier:
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
