from bst import BinarySearchTree


class BSTTraversal(BinarySearchTree):
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return results

    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)

            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        if self.root is not None:
            traverse(self.root)

        return results
    
    def dfs_post_order(self):
        results = []
        def traverse(current_node):

            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            
            results.append(current_node.value)

        if self.root is not None:
            traverse(self.root)


        return results
    
    def dfs_inorder(self):
        results = []
        def traverse(current_node):

            if current_node.left is not None:
                traverse(current_node.left)
            
            results.append(current_node.value)
            
            if current_node.right is not None:
                traverse(current_node.right)
            

        if self.root is not None:
            traverse(self.root)

        return results

    def is_valid_bst(self):
        results = []
        global is_valid
        is_valid = True
        def check_val(current_node):
            if current_node.left is not None:
                check_val(current_node.left)
            
            try:
                if results[-1] >= current_node.value:
                    global is_valid
                    is_valid = False
            except IndexError:
                pass
            finally:
                    results.append(current_node.value)

            if current_node.right is not None:
                check_val(current_node.right)
        if self.root is not None: 
            check_val(self.root)

        return is_valid 

    def kth_smallest(self, i):
        results = {}
        global k
        k = 1
        def liquidate_tree(cn):
            if cn.left is not None:
                liquidate_tree(cn.left)

            global k
            results[k] = cn.value
            k += 1

            if cn.right is not None:
                liquidate_tree(cn.right)


        if self.root is not None:
            liquidate_tree(self.root)
        else:
            return None

        return results.get(i, None)







if __name__ == "__main__":
    my_tree = BSTTraversal()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    
    print(my_tree.BFS())
    
    
    
    """
        EXPECTED OUTPUT:
        ----------------
        [47, 21, 76, 18, 27, 52, 82]
    
     """
    print(my_tree.dfs_pre_order())
    print(my_tree.dfs_post_order())
    print(my_tree.dfs_inorder())
    print(my_tree.is_valid_bst())

    print("-------Testing kth smallest---------")
    bst = BSTTraversal()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    
    print(bst.kth_smallest(1))  # Expected output: 2
    print(bst.kth_smallest(3))  # Expected output: 4
    print(bst.kth_smallest(6))  # Expected output: 7
    

