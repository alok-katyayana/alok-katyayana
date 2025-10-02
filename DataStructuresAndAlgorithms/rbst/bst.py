class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node


    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def contains(self, value):
        tmp = self.root
        return self.__r_contains(tmp, value)

    def __r_delete(self, prev_node, current_node, value):
        if current_node.value == value:
            if current_node.left is None and current_node.right is not None:
                if prev_node.right == current_node:
                    prev_node.right = current_node.right
                elif prev_node.left == current_node:
                    prev_node.left = current_node.right
            elif current_node.left is not None and current_node.right is None:
                if prev_node.right == current_node:
                    prev_node.right = current_node.left
                elif prev_node.left == current_node:
                    prev_node.left = current_node.left
            elif current_node.left is None and current_node.right is None:
                if prev_node.right == current_node:
                    prev_node.right = None 
                elif prev_node.left == current_node:
                    prev_node.left = None 

            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min

                self.__r_delete(current_node, current_node.right, sub_tree_min)


            return True

        if value < current_node.value:
            self.__r_delete(current_node, current_node.left, value)

        if value > current_node.value:
            self.__r_delete(current_node, current_node.right, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        
        return current_node.value

    def delete_node(self, value):
        if not self.contains(value):
            return False
        

        if value < self.root.value:
            self.__r_delete(self.root, self.root.left, value)

        if value > self.root.value:
            self.__r_delete(self.root, self.root.right, value)
    # The 'is_balanced' and 'inorder_traversal' methods will 
    # be used to test your code
    def is_balanced(self, node=None):
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
       
if __name__ == "__main__":
    
    ##########################################################
    ##   Test code below will print output to "User logs"   ##
    ##########################################################
    
    def check(expect, actual, message):
        print(message)
        print("EXPECTED:", expect)
        print("RETURNED:", actual)
        print("PASS" if expect == actual else "FAIL", "\n")
    
    
    # test_delete_node_no_children
    print("\n----- Test: Delete node with no children -----\n")
    bst = BinarySearchTree()
    values = [5, 3, 8]
    for v in values:
        print("Inserting value:", v)
        bst.insert(v)
    bst.delete_node(3)
    check(None, bst.root.left, "Left child of root after deleting 3:")
    
    
    # test_delete_node_only_left_child
    print("\n----- Test: Delete node with only left child -----\n")
    bst = BinarySearchTree()
    values = [5, 3, 8, 1]
    for v in values:
        print("Inserting value:", v)
        bst.insert(v)
    bst.delete_node(3)
    check(1, bst.root.left.value, "Left child of root after deleting 3:")
    
    
    # test_delete_node_only_right_child
    print("\n----- Test: Delete node with only right child -----\n")
    bst = BinarySearchTree()
    values = [5, 3, 8, 9]
    for v in values:
        print("Inserting value:", v)
        bst.insert(v)
    bst.delete_node(8)
    check(9, bst.root.right.value, "Right child of root after deleting 8:")
    
    
    # test_delete_node_two_children
    print("\n----- Test: Delete node with two children -----\n")
    bst = BinarySearchTree()
    values = [5, 3, 8, 1, 4, 7, 9]
    for v in values:
        print("Inserting value:", v)
        bst.insert(v)
    bst.delete_node(3)
    check(4, bst.root.left.value, "Left child of root after deleting 3:")
    
    
    # test_delete_root
    print("\n----- Test: Delete root -----\n")
    bst = BinarySearchTree()
    values = [5, 3, 8]
    for v in values:
        print("Inserting value:", v)
        bst.insert(v)
    bst.delete_node(5)
    check(8, bst.root.value, "Root value after deleting 5:")
    
    
    # test_delete_non_existent_node
    print("\n----- Test: Attempt to delete a non-existent node -----\n")
    bst = BinarySearchTree()
    values = [5, 3, 8]
    for v in values:
        print("Inserting value:", v)
        bst.insert(v)
    original_root_value = bst.root.value
    bst.delete_node(10)
    check(original_root_value, bst.root.value, "Root value after attempting to delete 10:")
