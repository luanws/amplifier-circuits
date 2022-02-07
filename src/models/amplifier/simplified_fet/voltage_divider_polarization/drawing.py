from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize

from .input import Input


def draw_void():
    drawing = Drawing()

    drawing += (transistor := elm.transistors.JFetP().right().reverse())

    drawing.push()
    drawing += elm.Resistor().at(transistor.drain).up().label('Rd').length(0.93*drawing.unit)
    drawing += elm.Line().left().length(drawing.unit/2)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.SourceV().up().reverse().label('Vdd')
    drawing += elm.Ground().left()

    drawing.pop()
    drawing += elm.Line().left().length(drawing.unit/2)
    drawing += elm.Resistor().down().label('R1')
    drawing += elm.Line().down().length(0.24*drawing.unit)
    drawing += elm.Dot()

    drawing.push()
    drawing += elm.Line().to(transistor.gate)

    drawing.pop()
    drawing.push()
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Capacitor().left().reverse().label('C1')
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Dot().label('Vi')

    drawing.pop()
    drawing += elm.Resistor().label('R2').length(0.93*drawing.unit)
    drawing += elm.Ground()

    drawing += elm.Resistor().label('Rs').down().at(transistor.source).length(0.78*drawing.unit)
    drawing += elm.Ground()

    drawing += elm.Dot().at(transistor.source)
    drawing += elm.Line().right().length(0.75*drawing.unit)
    drawing += elm.Capacitor().label('Cs').down().length(0.78*drawing.unit)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Dot().at(transistor.drain)
    drawing += elm.Capacitor().right().label('C2')
    drawing += elm.Dot().label('Vo')

    return drawing


def draw(amplifier_input: Input):
    Vdd = numerize(amplifier_input.Vdd, unit='V')
    R1 = numerize(amplifier_input.R1, unit='Ω')
    R2 = numerize(amplifier_input.R2, unit='Ω')
    Rd = numerize(amplifier_input.Rd, unit='Ω')
    Rs = numerize(amplifier_input.Rs, unit='Ω')

    drawing = Drawing()

    drawing += (transistor := elm.transistors.JFetP().right().reverse())

    drawing.push()
    drawing += elm.Resistor().at(transistor.drain).up().label(Rd).length(0.93*drawing.unit)
    drawing += elm.Line().left().length(drawing.unit/2)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.SourceV().up().reverse().label(Vdd)
    drawing += elm.Ground().left()

    drawing.pop()
    drawing += elm.Line().left().length(drawing.unit/2)
    drawing += elm.Resistor().down().label(R1)
    drawing += elm.Line().down().length(0.24*drawing.unit)
    drawing += elm.Dot()

    drawing.push()
    drawing += elm.Line().to(transistor.gate)

    drawing.pop()
    drawing.push()
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Capacitor().left().reverse().label('C1')
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Dot().label('Vi')

    drawing.pop()
    drawing += elm.Resistor().label(R2).length(0.93*drawing.unit)
    drawing += elm.Ground()

    drawing += elm.Resistor().label(Rs).down().at(transistor.source).length(0.78*drawing.unit)
    drawing += elm.Ground()

    drawing += elm.Dot().at(transistor.source)
    drawing += elm.Line().right().length(0.75*drawing.unit)
    drawing += elm.Capacitor().label('Cs').down().length(0.78*drawing.unit)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Dot().at(transistor.drain)
    drawing += elm.Capacitor().right().label('C2')
    drawing += elm.Dot().label('Vo')

    return drawing
