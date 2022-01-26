from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize
from sympy import numer

from .input import Input


def draw_void():
    drawing = Drawing()

    drawing += (transistor := elm.transistors.BjtNpn().right())
    drawing += elm.Line().up()
    drawing += elm.Line().left().length(drawing.unit/2)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.SourceV().up().label('Vcc').reverse()
    drawing += elm.Ground().left()

    drawing.pop()
    drawing += elm.Line().left().length(drawing.unit/2)
    drawing += elm.Resistor().down().label('Rb')
    drawing += elm.Line().down().length(0.24*drawing.unit)
    drawing += elm.Dot()

    drawing.push()
    drawing += elm.Line().to(transistor.base)

    drawing.pop()
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Capacitor2().label('C1').left()
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Dot().label('Vi')

    drawing += elm.Resistor().down().label('Re').at(transistor.emitter)
    drawing += elm.Ground()

    drawing += elm.Dot().at(transistor.emitter)
    drawing += elm.Capacitor2().label('C2').right()
    drawing += elm.Dot().label('Vo')

    return drawing


def draw(amplifier_input: Input):
    Vcc = numerize.format(amplifier_input.Vcc, 'V')
    Rb = numerize.format(amplifier_input.Rb, 'Ω')
    Re = numerize.format(amplifier_input.Re, 'Ω')

    drawing = Drawing()

    drawing += (transistor := elm.transistors.BjtNpn().right())
    drawing += elm.Line().up()
    drawing += elm.Line().left().length(drawing.unit/2)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.SourceV().up().label(Vcc).reverse()
    drawing += elm.Ground().left()

    drawing.pop()
    drawing += elm.Line().left().length(drawing.unit/2)
    drawing += elm.Resistor().down().label(Rb)
    drawing += elm.Line().down().length(0.24*drawing.unit)
    drawing += elm.Dot()

    drawing.push()
    drawing += elm.Line().to(transistor.base)

    drawing.pop()
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Capacitor2().label('C1').left()
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Dot().label('Vi')

    drawing += elm.Resistor().down().label(Re).at(transistor.emitter)
    drawing += elm.Ground()

    drawing += elm.Dot().at(transistor.emitter)
    drawing += elm.Capacitor2().label('C2').right()
    drawing += elm.Dot().label('Vo')

    return drawing
