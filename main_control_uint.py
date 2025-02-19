import ram
import acid.pythontwo.window.window as acid
import insration as ins

ramm = ram.ram(100)
dfo = ram.ram(100)
spm = ram.ram(100)
mode = 0  # Global mode variable

def Run_intract(intraction, opprants, j):
        global mode  # Access global mode

        # Operand handling
        if len(opprants) >= 1:
            a = int(opprants[0])
        if len(opprants) >= 2:
            b = int(opprants[1])
        if len(opprants) >= 3:
            c = int(opprants[2])
        if len(opprants) >= 4:
            d = int(opprants[3])
        if len(opprants) >= 5:
            e = int(opprants[4])

        # Instruction handling
        #print(ramm.data)
        if intraction == ins.nop:
            pass
        elif intraction == ins.add:
            ramm.write(c, ramm.read(a) + ramm.read(b))
        elif intraction == ins.sub:
            ramm.write(c, ramm.read(a) - ramm.read(b))
        elif intraction == ins.mul:
            ramm.write(c, ramm.read(a) * ramm.read(b))
        elif intraction == ins.div:
            if ramm.read(a) == 0 or ramm.read(b) == 0:
                ramm.write(c, 0)
            else:
                ramm.write(c, ramm.read(a) // ramm.read(b))
        elif intraction == ins.jmp:
            return a
        elif intraction == ins.jic:
            match d:
                case 0:
                    if ramm.read(a) == ramm.read(b):
                        return c
                case 1:
                    if ramm.read(a) < ramm.read(b):
                        return c
                case 2:
                    if ramm.read(a) > ramm.read(b):
                        return c
                case 3:
                    if ramm.read(a) != ramm.read(b):
                        return c

        elif intraction == ins.load:
            ramm.write(a, b)
        elif intraction == ins.store:
            ramm.write(a, ramm.read(b))
        elif intraction == ins.out:
            # Output instruction stores value in dfo
            mode = 1
            dfo.write(0, ramm.read(a))
            dfo.write(1, j)
            return 1
        elif intraction == ins.pout:
            # Print output (handle the output using dfo data)
            if mode == 1:
                mode = 0  # Switch back to user mode
                print(dfo.read(0))  # Output the value from dfo
                thing = dfo.read(1) + 1
                dfo.write(0, 0)
                dfo.write(1, 0)
                return thing  # Return the value (or could be used for other logic)
        elif intraction == ins.halt:
            mode = 1
            return 13
        elif intraction == ins.phalt:
            # Halt instruction
            if mode == 1:
                return "stop please I am going to die"  # Handle halting in kernel mode
        elif intraction == ins.init:
            mode = 1
            dfo.write(0, ramm.read(a))
            dfo.write(1, ramm.read(b))
            dfo.write(2, j)
            return 5
        elif intraction == ins.pinit:
            if mode == 1:
                screen = acid.window((dfo.read(0), dfo.read(1)), "hello frog user")
                screen.init()
                spm.write(0, screen)
                thing = dfo.read(2) + 1
                dfo.write(0, 0)
                dfo.write(1, 0)
                dfo.write(2, 0)
                return thing  # Return the value (or could be used for other logic)
        
        elif intraction == ins.mp:
            mode = 1
            dfo.write(0, ramm.read(a))
            dfo.write(1, ramm.read(b))
            dfo.write(2, ramm.read(c))
            dfo.write(3, ramm.read(d))
            dfo.write(4, ramm.read(e))
            dfo.write(5, j)
            return 9
        
        elif intraction == ins.pmp:
           if mode == 1:
                screen = spm.read(0)
                screen.makepixel((dfo.read(0), dfo.read(1)), (dfo.read(2), dfo.read(3), dfo.read(4)))
                thing = dfo.read(5) + 1
                dfo.write(0, 0)
                dfo.write(1, 0)
                dfo.write(2, 0)
                dfo.write(3, 0)
                dfo.write(4, 0)
                dfo.write(5, 0)
                return thing
        elif intraction == ins.loop:
            screen = spm.read(0)
            screen.loop()
        else:
            pass
        
        return j  # Return the input value `j` after processing
