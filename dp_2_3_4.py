# 이진트리의 depth() 연산 구현

class Node:    
    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        
        return max(l, r) + 1

class BinaryTree:
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0