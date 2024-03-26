# 양방향 연결 리스트 노드 삭제

def popAfter(self, prev):
    curr = prev.next
    next = curr.next
    pd = curr.data
    prev.next = next
    next.prev = prev
    self.nodeCount -= 1
        
    return pd


def popBefore(self, next):
    curr = next.prev
    prev = curr.prev
    pd = curr.data
    prev.next = next
    next.prev = prev
    self.nodeCount -= 1
        
    return pd


def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError
            
    if pos == self.nodeCount:
        next = self.tail
            
        return self.popBefore(next)
    elif pos == self.nodeCount:
        prev = self.head
    else:
        prev = self.getAt(pos - 1)
            
    return self.popAfter(prev)