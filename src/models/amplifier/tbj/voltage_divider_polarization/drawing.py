from schemdraw import Drawing
from schemdraw import elements as elm
from src.utils import numerize

from .input import Input


def __draw(
    R2: str, R1: str, Rc: str, Re: str, Vcc: str,
    Ci: str, Co: str, Ce: str, Rs: str, Rl: str
):
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
    drawing += elm.Line().right().length(0.75*drawing.unit)
    drawing += elm.Capacitor().label(Ce).down().length(0.78*drawing.unit)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Dot()
    drawing += elm.Capacitor().right().at(transistor.collector).label(Co).length(drawing.unit*1.5)

    drawing.push()
    drawing += elm.Dot()
    drawing += elm.Resistor().down().label(Rl).length(drawing.unit*1.25)
    drawing += elm.Ground()

    drawing.pop()
    drawing += elm.Line().right().length(drawing.unit/4)
    drawing += elm.Dot().label('Vo')

    return drawing


def draw_void():
    return __draw(
        R2='R2',
        R1='R1',
        Rc='Rc',
        Re='Re',
        Vcc='Vcc',
        Ci='Ci',
        Co='Co',
        Ce='Ce',
        Rs='Rs',
        Rl='Rl',
    )


def draw(amplifier_input: Input):
    R2 = numerize.format(amplifier_input.R2, unit='Ω')
    R1 = numerize.format(amplifier_input.R1, unit='Ω')
    Rc = numerize.format(amplifier_input.Rc, unit='Ω')
    Re = numerize.format(amplifier_input.Re, unit='Ω')
    Vcc = numerize.format(amplifier_input.Vcc, unit='V')
    Ci = numerize.format(amplifier_input.Ci, unit='F')
    Co = numerize.format(amplifier_input.Co, unit='F')
    Ce = numerize.format(amplifier_input.Ce, unit='F')
    Rs = numerize.format(amplifier_input.Rs, unit='Ω')
    Rl = numerize.format(amplifier_input.Rl, unit='Ω')

    return __draw(
        R2=R2,
        R1=R1,
        Rc=Rc,
        Re=Re,
        Vcc=Vcc,
        Ci=Ci,
        Co=Co,
        Ce=Ce,
        Rs=Rs,
        Rl=Rl,
    )
