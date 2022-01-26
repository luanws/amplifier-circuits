from abc import ABC, abstractstaticmethod


class Input(ABC):
    @abstractstaticmethod
    def get_parameter_names(self) -> list[str]:
        pass

    @abstractstaticmethod
    def get_parameter_units(self) -> list[str]:
        pass
