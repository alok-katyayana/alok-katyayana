class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node

        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1

        return True

    def print_stack(self):
        print(f"The height of the stack is {self.height}")
        tmp = self.top
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def pop(self):
        if self.top is None:
            return None

        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        self.height -= 1
        return tmp.value

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.value

    def is_empty(self):
        return self.height == 0

if __name__ == "__main__":
    stc = Stack()
    
    for i in range(10):
        stc.push(i)
    
    print(f"Peek : {stc.peek()}")
    stc.print_stack()
    
    x = 1
    while x is not None:
        x = stc.pop()
        print(x)
    
    stc.print_stack()
