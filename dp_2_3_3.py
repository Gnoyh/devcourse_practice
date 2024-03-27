# 우선순위 큐의 enqueue 연산 구현

def enqueue(self, x):
    node = Node(x)
    curr = self.queue.head
        
    while curr.next != self.queue.tail and x < curr.next.data:
        curr = curr.next
            
    self.queue.insertAfter(curr, node)