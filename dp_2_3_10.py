# 최대 힙에 새로운 원소 삽입

def insert(self, item):
    self.data.append(item)
    
    start = len(self.data) - 1
    
    while start > 1 and self.data[start // 2] < self.data[start]:
        self.data[start // 2], self.data[start] = self.data[start], self.data[start // 2]
        
        start //= 2