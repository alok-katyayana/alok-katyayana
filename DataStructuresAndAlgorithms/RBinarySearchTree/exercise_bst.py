from binary_search_tree import Node, BinarySearchTree

class ExerciseBST(BinarySearchTree):
    def __sorted_list_to_bst(self, nums, left, right):
        if left > right:
            return None
    
        mid = (left+right) // 2
        current = Node(nums[mid])
    
        current.left = self.__sorted_list_to_bst(nums, left, mid-1)
        current.right = self.__sorted_list_to_bst(nums, mid+1, right)
    
        return current 

    def sorted_list_to_bst(self, nums):
            self.root = self.__sorted_list_to_bst( nums, 0, len(nums) - 1)

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, current_node):
        if current_node is None:
            return None

        tmp = current_node.right
        current_node.right = current_node.left
        current_node.left = tmp

        current_node.left = self.__invert_tree(current_node.left)
        current_node.right = self.__invert_tree(current_node.right)

        return current_node










#  +====================================================+  
#  |  Test code below will print output to "User logs"  |
#  +====================================================+ 

def check_balanced_and_correct_traversal(bst, expected_traversal):
    is_balanced = bst.is_balanced()
    inorder = bst.inorder_traversal()
    print("Is balanced:", is_balanced)
    print("Inorder traversal:", inorder)
    print("Expected traversal:", expected_traversal)
    if is_balanced and inorder == expected_traversal:
        print("PASS: Tree is balanced and inorder traversal is correct.\n")
    else:
        print("FAIL: Tree is either not balanced or inorder traversal is incorrect.\n")

# Test: Convert an empty list
print("\n----- Test: Convert Empty List -----\n")
bst = ExerciseBST()
bst.sorted_list_to_bst([])
check_balanced_and_correct_traversal(bst, [])

# Test: Convert a list with one element
print("\n----- Test: Convert Single Element List -----\n")
bst = ExerciseBST()
bst.sorted_list_to_bst([10])
check_balanced_and_correct_traversal(bst, [10])

# Test: Convert a sorted list with odd number of elements
print("\n----- Test: Convert Sorted List with Odd Number of Elements -----\n")
bst = ExerciseBST()
bst.sorted_list_to_bst([1, 2, 3, 4, 5])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5])

# Test: Convert a sorted list with even number of elements
print("\n----- Test: Convert Sorted List with Even Number of Elements -----\n")
bst = ExerciseBST()
bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5, 6])

# Test: Convert a large sorted list
print("\n----- Test: Convert Large Sorted List -----\n")
bst = ExerciseBST()
large_sorted_list = list(range(1, 16))  # A list from 1 to 15
bst.sorted_list_to_bst(large_sorted_list)
check_balanced_and_correct_traversal(bst, large_sorted_list)




print("------------------------------------------------------\n")
print(f"Invert Exercise")

#  +====================================================+
#  |  Test code below will print output to "User logs"  |
#  +====================================================+

def tree_to_list(node):
    """Helper function to convert tree to list level-wise for easy comparison"""
    if not node:
        return []
    queue = [node]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:  # Clean up trailing None values
        result.pop()
    return result

def test_invert_binary_search_tree():
    print("\n--- Testing Inversion of Binary Search Tree ---")
    # Define test scenarios
    scenarios = [
        ("Empty Tree", [], []),
        ("Single Node", [1], [1]),
        ("Tree with Left Child", [2, 1], [2, None, 1]),
        ("Tree with Right Child", [1, 2], [1, 2]),
        ("Multi-Level Tree", [3, 1, 5, 2], [3, 5, 1, None, None, 2]),
        ("Invert Twice", [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
    ]

    for description, setup, expected in scenarios:
        bst = ExerciseBST()
        for num in setup:
            bst.insert(num)
        if description == "Invert Twice":
            bst.invert()  # First inversion
        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)
        print(f"\n{description}: {'Pass' if result == expected else 'Fail'}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")

test_invert_binary_search_tree()

