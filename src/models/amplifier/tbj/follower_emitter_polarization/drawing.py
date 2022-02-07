from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize

from .input import Input


def __draw(Vcc: str, Rb: str, Re: str, Ci: str, Co: str, Rs: str, Rl: str):
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
    drawing += elm.Capacitor2().label(Ci).left().length(drawing.unit*0.5)
    drawing += elm.Resistor().left().label(Rs)
    drawing += elm.Dot().label('Vi')

    drawing += elm.Resistor().down().label(Re).at(transistor.emitter)
    drawing += elm.Ground()

    drawing += elm.Dot().at(transistor.emitter)
    drawing += elm.Capacitor2().label(Co).right()

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Resistor().down().label(Rl)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Line().right().length(drawing.unit*0.25)
    drawing += elm.Dot().label('Vo')

    return drawing


def draw_void():
    return __draw(
        Vcc='Vcc',
        Rb='Rb',
        Re='Re',
        Ci='Ci',
        Co='Co',
        Rs='Rs',
        Rl='Rl',
    )


def draw(amplifier_input: Input):
    Vcc = numerize.format(amplifier_input.Vcc, unit='V')
    Rb = numerize.format(amplifier_input.Rb, unit='Ω')
    Re = numerize.format(amplifier_input.Re, unit='Ω')
    Ci = numerize.format(amplifier_input.Ci, unit='F')
    Co = numerize.format(amplifier_input.Co, unit='F')
    Rs = numerize.format(amplifier_input.Rs, unit='Ω')
    Rl = numerize.format(amplifier_input.Rl, unit='Ω')

    return __draw(
        Vcc=Vcc,
        Rb=Rb,
        Re=Re,
        Ci=Ci,
        Co=Co,
        Rs=Rs,
        Rl=Rl,
    )
