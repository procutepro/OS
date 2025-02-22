class ram:
    def __init__(self, storage):
        self.storage = storage
        self.data = []
        for i in range(self.storage):
            self.data.append(0)

    def write(self, postiion, info):
        self.data[int(postiion)] = info
    
    def read(self, postion):
        return self.data[int(postion)]
    
    def switch(self, pos1, pos2):
        temp = self.data[pos1]
        self.data[pos1] = self.data[pos2]
        self.data[pos2] = temp
        temp = ""