import main_control_uint as mcu

class computer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = self.spilt()
    
    def spilt(self):
        try:
            with open(self.file_path, 'r') as file:
                self.content = file.read()

            self.content = self.content.splitlines()
            
            for i in range(len(self.content)):
                self.content[i] = self.content[i].split()
        except:
            return 'lol no luck for you'
    
    def procues(self):
        j = 0
        while j < len(self.content):  # Prevent out-of-bounds errors

            i = self.content[j]

            if i:  # Make sure it's not an empty instruction
                opprants = i[1:]  # Get operands without modifying original
                task = mcu.Run_intract(i[0], opprants, j)

                if task == "stop plaseae i am going to die":
                    break  # Stop execution
                else:
                    task = int(task)

                if isinstance(task, int) and task != j:  
                    j = task  # Jump to new instruction
                else:
                    j += 1  # Move to next instruction
            else:
                j += 1

cpu = computer("binary.txt")
cpu.spilt()
cpu.procues()