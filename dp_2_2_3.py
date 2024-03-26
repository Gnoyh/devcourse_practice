# dummy head를 가지는 연결 리스트 노드 삭제

def popAfter(self, prev):
    curr = prev.next
    pd = curr.data
    prev.next = curr.next
        
    if prev.next == None:
        self.tail = prev
            
    self.nodeCount -= 1
        
    return pd


def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError
            
    if pos == 1:
        prev = self.head
    else:
        prev = self.getAt(pos - 1)
            
    return self.popAfter(prev)