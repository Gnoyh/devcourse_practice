# 이진 탐색 트리에서 노드의 삭제 연산 구현

def remove(self, key):
    node, parent = self.lookup(key)
        
    if node:
        cc = node.countChildren()
            
        if cc == 0:
            if parent:
                if key < parent.key:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        elif cc == 1:
        	if node.left:
                child = node.left
            else:
                child = node.right
                    
            if parent:
                if key < parent.key:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
        else:
            parent = node
            successor = node.right
                
            while successor.left:
            	parent = successor
                successor = successor.left
                    
            node.key = successor.key
            node.data = successor.data
                
            if successor.key < parent.key:
            	parent.left = successor.right
            else:
            	parent.right = successor.right
    else:
    	raise KeyError