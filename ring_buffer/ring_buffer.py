class RingBuffer:
    def __init__(self, capacity):
        self.capacity = 5
        self.data = []
        
    class Full:
        def append(self, item):
            self.data[self.cur] = item
            self.cur = (self.cur + 1) % self.capactiy
        def get(self):
            return self.data[:self.cur] + self.data[:self.cur]
    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.cur = 0
            
    def get(self):
        return self.data