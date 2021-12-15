from schemdraw import Drawing
from schemdraw import elements as elm

from .input import Input


def draw_void():
    drawing = Drawing()

    drawing += (transistor := elm.transistors.JFetP().reverse().right())
    drawing += elm.Line().left().length(drawing.unit/2)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Resistor().down().label('Rg')
    drawing += elm.SourceV().down().label('Vgg').length(drawing.unit/2)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Capacitor().left()
    drawing += elm.Dot().label('Vi')

    drawing += elm.Resistor().up().at(transistor.drain).label('Rd')
    drawing += elm.SourceV().label('Vdd').reverse().length(drawing.unit/2)
    drawing += elm.Ground().left()

    drawing += elm.Line().down().at(transistor.source).length(drawing.unit/2)
    drawing += elm.Line().down().length(0.86*drawing.unit)
    drawing += elm.Ground()

    drawing += elm.Capacitor().right().at(transistor.drain).label('C2')
    drawing += elm.Dot().label('Vo')

    drawing += elm.Dot().at(transistor.gate).label('G')
    drawing += elm.Dot().at(transistor.drain).label('D').up()
    drawing += elm.Dot().at(transistor.source).label('S').down()

    return drawing


def draw(amplifier_input: Input):
    drawing = Drawing()

    drawing += (transistor := elm.transistors.JFetP().reverse().right())
    drawing += elm.Line().left().length(drawing.unit/2)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Resistor().down().label('Rg')
    drawing += elm.SourceV().down().label('Vgg').length(drawing.unit/2)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Capacitor().left()
    drawing += elm.Dot().label('Vi')

    drawing += elm.Resistor().up().at(transistor.drain).label('Rd')
    drawing += elm.SourceV().label('Vdd').reverse().length(drawing.unit/2)
    drawing += elm.Ground().left()

    drawing += elm.Line().down().at(transistor.source).length(drawing.unit/2)
    drawing += elm.Line().down().length(0.86*drawing.unit)
    drawing += elm.Ground()

    drawing += elm.Capacitor().right().at(transistor.drain).label('C2')
    drawing += elm.Dot().label('Vo')

    drawing += elm.Dot().at(transistor.gate).label('G')
    drawing += elm.Dot().at(transistor.drain).label('D').up()
    drawing += elm.Dot().at(transistor.source).label('S').down()

    return drawing
