# 연결 리스트 순회

def traverse(self):
    ll = []
    curr = self.head
        
    while curr != None:
        ll.append(curr.data)
            
        curr = curr.next
            
    return ll