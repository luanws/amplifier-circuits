from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize

from .input import Input


def __draw(R2: str, R1: str, Re: str, Vcc: str, Ci: str, Co: str, Rs: str, Rl: str):
    drawing = Drawing()

    drawing += (transistor := elm.transistors.BjtNpn().right())

    drawing.push()
    drawing += elm.Line().up()
    drawing += elm.Line().left().length(drawing.unit/2)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.SourceV().up().reverse().label(Vcc)
    drawing += elm.Ground().left()

    drawing.pop()
    drawing += elm.Line().left().length(drawing.unit/2)
    drawing += elm.Resistor().down().label(R1)
    drawing += elm.Line().down().length(0.24*drawing.unit)
    drawing += elm.Dot()

    drawing.push()
    drawing += elm.Line().to(transistor.base)

    drawing.pop()
    drawing.push()
    drawing += elm.Line().left().length(drawing.unit/4)
    drawing += elm.Capacitor().left().reverse().label(Ci).length(drawing.unit*0.5)
    drawing += elm.Resistor().left().label(Rs)
    drawing += elm.Dot().label('Vi')

    drawing.pop()
    drawing += elm.Resistor().label(R2)
    drawing += elm.Ground()

    drawing += elm.Resistor().label(Re).down().at(transistor.emitter).length(0.78*drawing.unit)
    drawing += elm.Ground()

    drawing += elm.Dot().at(transistor.emitter)
    drawing += elm.Capacitor().right().label(Co)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Resistor().down().label(Rl).length(0.78*drawing.unit)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Line().right().length(drawing.unit*0.25)
    drawing += elm.Dot().label('Vo')

    return drawing


def draw_void():
    return __draw(
        Vcc='Vcc',
        R1='R1',
        R2='R2',
        Re='Re',
        Ci='Ci',
        Co='Co',
        Rs='Rs',
        Rl='Rl',
    )


def draw(amplifier_input: Input):
    Vcc = numerize.format(amplifier_input.Vcc, unit='V')
    R1 = numerize.format(amplifier_input.R1, unit='Ω')
    R2 = numerize.format(amplifier_input.R2, unit='Ω')
    Re = numerize.format(amplifier_input.Re, unit='Ω')
    Ci = numerize.format(amplifier_input.Ci, unit='F')
    Co = numerize.format(amplifier_input.Co, unit='F')
    Rs = numerize.format(amplifier_input.Rs, unit='Ω')
    Rl = numerize.format(amplifier_input.Rl, unit='Ω')

    return __draw(
        Vcc=Vcc,
        R1=R1,
        R2=R2,
        Re=Re,
        Ci=Ci,
        Co=Co,
        Rs=Rs,
        Rl=Rl,
    )
