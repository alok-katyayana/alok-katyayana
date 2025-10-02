"""
   This Module Consists of class for Binary Search Tree 
   and a helper Node class
"""

class Node:
    """ 
       This Class consists of each node in a binary search tree.
       A node will have two children called left and right
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
       This class is an abstraction for a Binary Search Tree. There is a pointer to the root
       and the rest of the tree can be traversed from the root. By the definition of binary search 
       tree, all the nodes to the left of the root will have value less than the value at root and
       all the nodes to the right of the root will have value greater that the value at root (
       consequently for each subsequent node.)
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
           Insert a new node into the tree and place it to it's correct position so that the 
           property of a binary search tree is maintained.
        """

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
        """
           Returns true if the value is present in the Binary Search Tree,
           else returns False.
        """
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
