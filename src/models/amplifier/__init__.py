from abc import ABC, abstractmethod

from . import drawing
from .input import Input
from .output import Output


class Amplifier(ABC):
    input: Input

    @abstractmethod
    def draw(self):
        pass

    def draw_equivalent(self):
        output = self()
        return drawing.draw_equivalent_model(output)

    @abstractmethod
    def __call__(self) -> Output:
        pass
