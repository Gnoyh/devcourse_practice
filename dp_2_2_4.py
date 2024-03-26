# 양방향 연결 리스트 역방향 순회

def reverse(self):
    dll = []
    curr = self.tail
        
    while curr.prev.prev:
        curr = curr.prev
        dll.append(curr.data)
            
    return dll