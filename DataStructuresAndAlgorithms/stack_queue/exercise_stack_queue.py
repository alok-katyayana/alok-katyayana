from queue import *
from stack import *


## Stack Exercises

# Parentheses Balanced

def is_balanced_parentheses(vstr:str):
    stc = Stack()
    for alb in vstr:
        if alb == "(":
            stc.push(alb)
        elif alb == ")":
            if stc.height == 0 or stc.pop() != "(":
                return False

    return stc.height == 0

def reverse_string(vstr:str):
    stc = Stack()
    for alb in vstr:
        stc.push(alb)

    res = ""
    while stc.height > 0:
        res += str(stc.pop())

    return res

def sort_stack(stack:Stack):
    sorted_stack = Stack()

    while not stack.is_empty():
        tmp = stack.pop()
        
        while ( not sorted_stack.is_empty()
               and sorted_stack.peek() > tmp):
               stack.push(sorted_stack.pop())

        sorted_stack.push(tmp)
    
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())


    return sorted_stack



    


print("------------\nTest Stack Exercises")
print("Test Parentheses balanced")

vstr =  "(()"

res = is_balanced_parentheses(vstr)

print(res)


print("Test Reversal of String")
my_string = 'hello'

print ( reverse_string(my_string) )



print("Test sort stack")
st = Stack(); st.push(7); st.push(1); st.push(10); st.push(-3);
st.print_stack()
sort_stack(st)
st.print_stack()

