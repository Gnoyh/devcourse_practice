# 양방향 연결 리스트로 구현하는 큐

class LinkedListQueue:
	def __init__(self):
    	self.data = DoublyLinkedList()
        
    def size(self):
    	return self.data.getLength()
        
    def isEmpty(self):
    	return self.size() == 0
        
    def enqueue(self, item):
    	node = Node(item)
        self.data.insertAt(self.size() + 1, node)
        
    def dequeue(self):
    	return self.data.popAt(1)
        
    def peek(self):
    	return self.data.getAt(1).data