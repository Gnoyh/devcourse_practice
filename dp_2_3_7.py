# 이진트리의 넓이 우선 순회

def bft(self):
    traversal = []
        
    q = ArrayQueue()
        
    if self.root:
        q.enqueue(self.root)
        
    while not q.isEmpty():
        parent = q.dequeue()
            
        if parent.left:
            q.enqueue(parent.left)
            
        if parent.right:
            q.enqueue(parent.right)
                
        traversal.append(parent.data)
            
    return traversal