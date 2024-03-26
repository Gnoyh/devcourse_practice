# 양방향 연결 리스트의 병합

def concat(self, L):
    self.tail.prev.next = L.head.next
    L.head.next.prev = self.tail.prev
    self.nodeCount += L.nodeCount
    self.tail = L.tail