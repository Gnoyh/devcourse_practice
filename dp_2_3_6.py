# 이진트리의 후위순회 연산 구현

class Node:
    def postorder(self):
        traversal = []
        
        if self.left:
        	traversal += self.left.postorder()
        
        if self.right:
        	traversal += self.right.postorder()
            
        traversal.append(self.data)
            
        return traversal

class BinaryTree:
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []