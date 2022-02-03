from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize

from .input import Input


def draw_void():
    drawing = Drawing()

    drawing += (transistor := elm.transistors.JFetP().right().reverse())

    drawing += elm.SourceV().at(transistor.drain).up().label('Vdd').reverse()
    drawing += elm.Ground().left()

    drawing += elm.Line().left().at(transistor.gate).length(drawing.unit/4)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Resistor().down().label('Rg')
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Capacitor().label('C1').left()
    drawing += elm.Dot().label('Vi')

    drawing += elm.Dot().at(transistor.source).down()

    drawing.push()
    drawing += elm.Resistor().down().label('Rs').length(drawing.unit*0.857)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Capacitor().label('C2').right()
    drawing += elm.Dot().label('Vo')

    return drawing


def draw(amplifier_input: Input):
    Vdd = numerize.format(amplifier_input.Vdd, unit='V')
    Rg = numerize.format(amplifier_input.Rg, unit='Ω')
    Rs = numerize.format(amplifier_input.Rs, unit='Ω')

    drawing = Drawing()

    drawing += (transistor := elm.transistors.JFetP().right().reverse())

    drawing += elm.SourceV().at(transistor.drain).up().label(Vdd).reverse()
    drawing += elm.Ground().left()

    drawing += elm.Line().left().at(transistor.gate).length(drawing.unit/4)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Resistor().down().label(Rg)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Capacitor().label('C1').left()
    drawing += elm.Dot().label('Vi')

    drawing += elm.Dot().at(transistor.source).down()

    drawing.push()
    drawing += elm.Resistor().down().label(Rs).length(drawing.unit*0.857)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Capacitor().label('C2').right()
    drawing += elm.Dot().label('Vo')

    return drawing
