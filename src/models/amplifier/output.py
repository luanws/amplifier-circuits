from abc import ABC, abstractstaticmethod


class Output(ABC):
    @abstractstaticmethod
    def get_parameter_names(self) -> list[str]:
        return ['Zi', 'Zo', 'Avnl']

    @abstractstaticmethod
    def get_parameter_units(self) -> list[str]:
        return ['Ω', 'Ω', '']
