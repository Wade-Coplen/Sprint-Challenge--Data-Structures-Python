class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.current = 0
            self.__class__ = FullBuffer
    def get(self):
        return self.data
class FullBuffer:
    def __init__(self, n):
        return
    def append(self, item):
        self.data[self.current]= item
        self.current=(self.current + 1) % self.capacity     
    def get(self):
        return self.data[:self.current] + self.data[self.current:]
    

        #if len(self.data) == self.capacity:
            #self.cur = 0
            
    