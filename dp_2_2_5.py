# 양방향 연결 리스트 노드 삽입

def insertBefore(self, next, newNode):
    prev = next.prev
    newNode.prev = prev
    newNode.next = next
    prev.next = newNode
    next.prev = newNode
    self.nodeCount += 1
        
    return True