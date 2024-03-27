# 이진 탐색 트리의 원소 삽입 연산 구현

def insert(self, key, data):
    if key < self.key:
        if self.left:
            return self.left.insert(key, data)
        else:
            self.left = Node(key, data)
    elif key > self.key:
        if self.right:
            return self.right.insert(key, data)
        else:
            self.right = Node(key, data)
    else:
        raise KeyError