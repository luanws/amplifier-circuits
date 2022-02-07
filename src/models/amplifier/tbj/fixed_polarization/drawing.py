from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize

from .input import Input


def __draw(Rc: str, Rb: str, Vcc: str, Rs: str, Rl: str, Ci: str, Co: str):
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
    drawing += elm.Capacitor().left().reverse().label(Ci).length(0.5*drawing.unit)
    drawing += elm.Resistor().left().label(Rs)
    drawing += elm.Dot().label('Vi')

    drawing += elm.Line().at(transistor.emitter).down().length(drawing.unit*0.53)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Dot()
    drawing += elm.Capacitor().right().label(Co)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Resistor().down().label(Rl)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Line().right().length(drawing.unit/4)
    drawing += elm.Dot().label('Vo')

    return drawing


def draw_void():
    return __draw(
        Rc='Rc',
        Rb='Rb',
        Vcc='Vcc',
        Rs='Rs',
        Rl='Rl',
        Ci='Ci',
        Co='Co',
    )


def draw(amplifier_input: Input):
    Rc = numerize.format(amplifier_input.Rc, unit='Ω')
    Rb = numerize.format(amplifier_input.Rb, unit='Ω')
    Vcc = numerize.format(amplifier_input.Vcc, unit='V')
    Rs = numerize.format(amplifier_input.Rs, unit='Ω')
    Rl = numerize.format(amplifier_input.Rl, unit='Ω')
    Ci = numerize.format(amplifier_input.Ci, unit='F')
    Co = numerize.format(amplifier_input.Co, unit='F')

    return __draw(
        Rc=Rc,
        Rb=Rb,
        Vcc=Vcc,
        Rs=Rs,
        Rl=Rl,
        Ci=Ci,
        Co=Co,
    )
