from schemdraw import Drawing
from schemdraw import elements as elm

from .output import Output


def draw_equivalent_model_void():
    drawing = Drawing()
    drawing += elm.Ground()
    drawing += elm.SourceSin().reverse().label('Vi')
    drawing += elm.Line().right()
    drawing += elm.Resistor().down().label('Zi')
    drawing += elm.Ground()
    drawing += elm.Dot()
    drawing += elm.Line().right()
    drawing += elm.SourceControlledI().reverse().label('βIb')
    drawing += elm.Resistor().right().label('Zo')
    drawing += elm.Resistor().down().label('Rl')
    drawing += elm.Ground()

    return drawing.draw()


def draw_equivalent_model(output: Output):
    Zi = str(round(output.Zi, 2))
    Zo = str(round(output.Zo, 2))
    drawing = Drawing()
    drawing += elm.Ground()
    drawing += elm.SourceSin().reverse().label('Vi')
    drawing += elm.Line().right()
    drawing += elm.Resistor().down().label(Zi)
    drawing += elm.Ground()
    drawing += elm.Dot()
    drawing += elm.Line().right()
    drawing += elm.SourceControlledI().reverse().label('βIb')
    drawing += elm.Resistor().right().label(Zo)
    drawing += elm.Resistor().down().label('Rl')
    drawing += elm.Ground()

    return drawing.draw()
