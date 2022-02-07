from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize

from .input import Input


def draw_void():
    drawing = Drawing()

    drawing += (transistor := elm.transistors.BjtNpn().right())

    drawing.push()
    drawing += elm.Resistor().up().label('Rc')
    drawing += elm.Line().left().length(drawing.unit/2)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.SourceV().up().reverse().label('Vcc')
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
    drawing += elm.Capacitor().left().reverse().label('Ci')
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Dot().label('Vi')

    drawing += elm.Line().at(transistor.emitter).down().length(3*drawing.unit/4)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Dot()
    drawing += elm.Capacitor().right().label('Co')
    drawing += elm.Dot().label('Vo')

    return drawing


def draw(amplifier_input: Input):
    Rc = numerize.format(amplifier_input.Rc, unit='Ω')
    Rb = numerize.format(amplifier_input.Rb, unit='Ω')
    Vcc = numerize.format(amplifier_input.Vcc, unit='V')

    drawing = Drawing()

    drawing += (transistor := elm.transistors.BjtNpn().right())

    drawing.push()
    drawing += elm.Resistor().up().label(Rc)
    drawing += elm.Line().left().length(drawing.unit/2)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.SourceV().up().reverse().label(Vcc)
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
    drawing += elm.Capacitor().left().reverse().label('Ci')
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Dot().label('Vi')

    drawing += elm.Line().at(transistor.emitter).down().length(3*drawing.unit/4)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Dot()
    drawing += elm.Capacitor().right().label('Co')
    drawing += elm.Dot().label('Vo')

    return drawing
