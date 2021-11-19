from schemdraw import Drawing
from schemdraw import elements as elm

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
    drawing += elm.SourceSin().down().label('Vi').reverse()
    drawing += elm.Line().right()
    drawing += elm.Line().right().length(drawing.unit/2)
    drawing += elm.Ground().right()
    drawing += elm.Dot()
    drawing += elm.Line().right()

    drawing.push()
    drawing += elm.Resistor().up().label('Re').to(transistor.emitter)
    drawing += elm.Capacitor2().label('C2').right()
    drawing += elm.Dot()

    drawing.pop()
    drawing += elm.Line().right()
    drawing += elm.Dot()

    return drawing


def draw(amplifier_input: Input):
    Vcc = str(round(amplifier_input.Vcc, 2))
    Rb = str(round(amplifier_input.Rb, 2))
    Re = str(round(amplifier_input.Re, 2))

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
    drawing += elm.SourceSin().down().label('Vi').reverse()
    drawing += elm.Line().right()
    drawing += elm.Line().right().length(drawing.unit/2)
    drawing += elm.Ground().right()
    drawing += elm.Dot()
    drawing += elm.Line().right()

    drawing.push()
    drawing += elm.Resistor().up().label(Re).to(transistor.emitter)
    drawing += elm.Capacitor2().label('C2').right()
    drawing += elm.Dot()

    drawing.pop()
    drawing += elm.Line().right()
    drawing += elm.Dot()

    return drawing
