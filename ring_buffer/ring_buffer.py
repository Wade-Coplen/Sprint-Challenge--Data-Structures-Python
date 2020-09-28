class RingBuffer:
    def __init__(self, capacity):
        self.capacity = 5
        self.data = []
        
    def append(self, item):
        self.data.append(item)
        #if len(self.data) == self.capacity:
            #self.cur = 0
            
    def get(self):
        return self.data