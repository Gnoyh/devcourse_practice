# 환형 큐 구현

def enqueue(self, x):
    if self.isFull():
        raise IndexError
        
    self.rear = (self.rear + 1) % self.maxCount
    self.data[self.rear] = x
    self.count += 1
        
def dequeue(self):
    if self.isEmpty():
        raise IndexError
            
    self.front = (self.front + 1) % self.maxCount
    x = self.data[self.front]
    self.count -= 1
        
    return x
        
def peek(self):
    if self.isEmpty():
        raise IndexError
            
    return self.data[(self.front + 1) % self.maxCount]