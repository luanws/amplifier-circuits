from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize

from .input import Input


def draw_void():
    drawing = Drawing()

    drawing += (transistor := elm.transistors.JFetP().reverse().right())
    drawing += elm.Line().left()

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Line().up().length(drawing.unit*0.3)
    drawing += elm.Resistor().up().label('Rg')
    drawing += elm.SourceV().up().label('Vgg').length(drawing.unit/2)
    drawing += elm.Ground().left()

    drawing.pop()
    drawing += elm.Capacitor().left()
    drawing += elm.Dot().label('Vi')

    drawing += elm.Resistor().up().at(transistor.drain).label('Rd')
    drawing += elm.SourceV().label('Vdd').reverse().length(drawing.unit/2)
    drawing += elm.Ground().left()

    drawing += elm.Line().at(transistor.source).down().length(drawing.unit/8)
    drawing += elm.Ground()

    drawing += elm.Dot().at(transistor.drain)
    drawing += elm.Capacitor().right().label('C2')
    drawing += elm.Dot().label('Vo')

    return drawing


def draw(amplifier_input: Input):
    Vdd = numerize.format(amplifier_input.Vdd, unit='V')
    Vgg = numerize.format(amplifier_input.Vgg, unit='V')
    Rd = numerize.format(amplifier_input.Rd, unit='Ω')
    Rg = numerize.format(amplifier_input.Rg, unit='Ω')

    drawing = Drawing()

    drawing += (transistor := elm.transistors.JFetP().reverse().right())
    drawing += elm.Line().left()

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Line().up().length(drawing.unit*0.3)
    drawing += elm.Resistor().up().label(Rg)
    drawing += elm.SourceV().up().label(Vgg).length(drawing.unit/2)
    drawing += elm.Ground().left()

    drawing.pop()
    drawing += elm.Capacitor().left()
    drawing += elm.Dot().label('Vi')

    drawing += elm.Resistor().up().at(transistor.drain).label(Rd)
    drawing += elm.SourceV().label(Vdd).reverse().length(drawing.unit/2)
    drawing += elm.Ground().left()

    drawing += elm.Line().at(transistor.source).down().length(drawing.unit/8)
    drawing += elm.Ground()

    drawing += elm.Dot().at(transistor.drain)
    drawing += elm.Capacitor().right().label('C2')
    drawing += elm.Dot().label('Vo')

    return drawing
