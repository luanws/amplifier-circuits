from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize

from .output import Output


def __draw_equivalent_model(Zi: str, Zo: str):
    drawing = Drawing()
    drawing += elm.Dot().label('Vi')
    drawing += elm.Line().right()
    drawing += elm.Resistor().down().label(Zi)

    drawing.push()
    drawing += elm.Line().right().color('white').length(drawing.unit*0.5)
    drawing += elm.Line().up().color('white').length(drawing.unit*0.25)
    drawing += elm.Ground()
    drawing += elm.SourceControlledI().up().length(drawing.unit*0.5)
    drawing += elm.Line().right().length(drawing.unit*0.25)
    drawing += elm.Line().down().length(drawing.unit*0.25)
    drawing += elm.Resistor().right().label(Zo)
    drawing += elm.Dot().label('Vo')

    drawing.pop()
    drawing += elm.Ground()

    return drawing


def draw_equivalent_model_void():
    return __draw_equivalent_model('Zi', 'Zo')


def draw_equivalent_model(output: Output):
    Zi = numerize.format(output.Zi, unit='Ω')
    Zo = numerize.format(output.Zo, unit='Ω')
    return __draw_equivalent_model(Zi, Zo)
