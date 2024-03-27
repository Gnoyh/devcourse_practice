# 최대 힙에서의 원소 삭제

def maxHeapify(self, i):
    left = i * 2
    right = i * 2 + 1
    smallest = i
    
    if left < len(self.data) and self.data[left] > self.data[smallest]:
        smallest = left
        
    if right < len(self.data) and self.data[right] > self.data[smallest]:
        smallest = right
        
    if smallest != i:
        self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
        self.maxHeapify(smallest)