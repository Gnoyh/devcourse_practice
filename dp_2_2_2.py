# 연결 리스트 노드 삭제

def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError
            
    if pos == 1:
        curr = self.head
        pd = curr.data
        self.head = curr.next
            
        if pos == self.nodeCount:
            self.tail = None
    else:
        prev = self.getAt(pos - 1)
        curr = prev.next
        pd = curr.data
        prev.next = curr.next
            
        if pos == self.nodeCount:
            self.tail = prev
                    
    self.nodeCount -= 1
        
    return pd