import ram 
import pygame.mouse as pg
from acid.pythontwo.window.window import window  # Corrected import
import insration as ins

ramm = ram.ram(100)
dfo = ram.ram(100)
spm = ram.ram(100)
mode = 0  # Global mode variable

def Run_intract(intraction, opprants, j):
    global mode  # Access global mode

    # Operand handling
    operands = [opprants[i] if i < len(opprants) else None for i in range(7)]
    a, b, c, d, e, f, g = operands

    # Instruction handling
    if intraction == ins.nop:
        pass
    elif intraction == ins.add:
        ramm.write(c, ramm.read(a) + ramm.read(b))
    elif intraction == ins.sub:
        ramm.write(c, ramm.read(a) - ramm.read(b))
    elif intraction == ins.mul:
        ramm.write(c, ramm.read(a) * ramm.read(b))
    elif intraction == ins.div:
        ramm.write(c, 0 if ramm.read(a) == 0 or ramm.read(b) == 0 else ramm.read(a) // ramm.read(b))
    elif intraction == ins.jmp:
        print("ok")
        return a
    elif intraction == ins.jic:
        match d:
            case 0 if ramm.read(a) == ramm.read(b): return c
            case 1 if ramm.read(a) < ramm.read(b): return c
            case 2 if ramm.read(a) > ramm.read(b): return c
            case 3 if ramm.read(a) != ramm.read(b): return c
    elif intraction == ins.load:
        ramm.write(a, str(b) if c == "s" else int(b))
    elif intraction == ins.store:
        ramm.write(a, ramm.read(b))
    elif intraction == ins.out:
        mode = 1
        dfo.write(0, ramm.read(a))
        dfo.write(1, j)
        return 1
    elif intraction == ins.pout and mode == 1:
        mode = 0
        print(dfo.read(0))
        thing = dfo.read(1) + 1
        dfo.write(0, 0)
        dfo.write(1, 0)
        return thing
    elif intraction == ins.halt:
        mode = 1
        return 13
    elif intraction == ins.phalt and mode == 1:
        mode = 0
        return "stop please I am going to die"
    elif intraction == ins.init:
        mode = 1
        dfo.write(0, ramm.read(a))
        dfo.write(1, ramm.read(b))
        dfo.write(2, j)
        return 5
    elif intraction == ins.pinit and mode == 1:
        mode = 0
        screen = window((dfo.read(0), dfo.read(1)), "hello frog user")
        screen.init()
        spm.write(0, screen)
        thing = dfo.read(2) + 1
        dfo.write(0, 0)
        dfo.write(1, 0)
        dfo.write(2, 0)
        return thing
    elif intraction == ins.mp:
        mode = 1
        for i in range(5):
            dfo.write(i, ramm.read(operands[i]))
        dfo.write(5, j)
        return 9
    elif intraction == ins.pmp and mode == 1:
        mode = 0
        screen = spm.read(0)
        screen.makepixel((dfo.read(0), dfo.read(1)), (dfo.read(2), dfo.read(3), dfo.read(4)))
        thing = dfo.read(5) + 1
        for i in range(6):
            dfo.write(i, 0)
        return thing
    elif intraction == ins.mr:
        mode = 1
        for i in range(7):
            dfo.write(i, ramm.read(operands[i]))
        dfo.write(7, j)
        return 13
    elif intraction == ins.pmr and mode == 1:
        mode = 0
        screen = spm.read(0)
        screen.MakeRect((dfo.read(0), dfo.read(1)), (dfo.read(2), dfo.read(3)), (dfo.read(4), dfo.read(5), dfo.read(6)))
        thing = dfo.read(7) + 1
        for i in range(8):
            dfo.write(i, 0)
        return thing
    elif intraction == ins.gmp:
        pos = pg.get_pos()
        print(pos)
        ramm.write(a, pos[0])
        ramm.write(b, pos[1])
    elif intraction == ins.loop:
        screen = spm.read(0)
        screen.loop()
        spm.write(0, screen)
    return j