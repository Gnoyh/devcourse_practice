# 이진트리의 전위순회 연산 구현

class Node:
    def preorder(self):
        traversal = []
        
        traversal.append(self.data)
        
        if self.left:
        	traversal += self.left.preorder()
        
        if self.right:
        	traversal += self.right.preorder()
            
        return traversal

class BinaryTree:
    def preorder(self):
        if self.root:
        	return self.root.preorder()
        else:
        	return []