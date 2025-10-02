class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        nn = Node(value)

        if self.root is None:
            self.root = nn
            return True

        tmp = self.root
        while True:
            if value == tmp.value:
                return False

            if value < tmp.value:
                if tmp.left is None:
                    tmp.left = nn
                    return True
                tmp = tmp.left
            
            if value > tmp.value:
                if tmp.right is None:
                    tmp.right = nn
                    return True
                tmp = tmp.right
    
    def contains(self, value):
        tmp = self.root

        while tmp is not None:
            if tmp.value == value:
                return True
            if value < tmp.value:
                tmp = tmp.left
            else:
                tmp = tmp.right

        return False

if __name__ == "__main__":
    bst = BinarySearchTree()
    
    bst.insert(5)
    bst.insert(4)
    bst.insert(7)

    print(bst.root.value)
    print(bst.root.left.value)
    print(bst.root.right.value)

    print(bst.contains(5))
    print(bst.contains(4))
    print(bst.contains(7))
    print(bst.contains(10))

