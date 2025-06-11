from linkedlist import LinkedList, Node

#
# Find Middle Node

def return_middle_node(ll):
    pointer1 = ll.head
    pointer2 = ll.head
    
    while pointer1 is not None and pointer1.next is not None:
        pointer2 = pointer2.next
        #print(pointer1.value)
        #try:
        pointer1 = pointer1.next.next
        #except AttributeError:
        #    break

    return pointer2

def has_loop(ll):
    pointer1 = ll.head
    pointer2 = ll.head

    while pointer1 is not None and pointer1.next is not None:
        pointer1 = pointer1.next.next
        pointer2 = pointer2.next

        if pointer1 == pointer2:
            return True

    return False

def k_th_from_end(ll, k):
    pointer1 = ll.head
    pointer2 = ll.head
    for _ in range(k):
        pointer1 = pointer1.next

    while pointer1 is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer2
        
def remove_duplicates(ll):
    holder = set()
    while ll.head is not None:
        holder.add(ll.pop_first().value)

    for elm in holder:
        ll.append(elm)

    return ll

def binary_to_decimal(ll):
    res = 0
    tmp = ll.head
    i = 0
    while tmp is not None:
        res = (2 * res) + (tmp.value* (2**i))
        i +=0
        tmp = tmp.next

    return res

def partition_list(ll, x):
    d1 = Node("dummy1")
    d2 = Node("dummy2")
    p1 = d1
    p2 = d2
    
    tmp = ll.head
    while tmp is not None:
        if tmp.value < x:
            p1.next = tmp
            p1 = p1.next
        else:
            p2.next = tmp
            p2 = p2.next
        tmp = tmp.next
    
    p2.next = None
    p1.next = d2.next
    ll.head = d1.next
    ll.Tail = p2
    p1 = None
    p2 = None
    d1 = None
    d2 = None

    return ll

def reverse_between(ll, start, end):
    d = Node("dumdum")
    d.next = ll.head
    prev = d
    for i in range(start):
        prev = prev.next
    
    cur = prev.next

    for i in range(end-start):
        tm = cur.next
        cur.next = tm.next
        tm.next = prev.next
        prev.next = tm

    ll.head = d.next

    return ll

def swap_pairs(ll):
    d = Node("dumdum")
    d.next = ll.head

    prev = d
    cur = ll.head

    while cur is not None and cur.next is not None:
        tm = cur.next
        prev.next = tm
        cur.next = tm.next 
        tm.next = cur

        prev = cur
        cur = cur.next
    ll.head = d.next
    return ll


print("---------------------Test Midde Node-----------------------------------------------")
omnll = LinkedList(1); omnll.append(2); omnll.append(3); omnll.append(4); omnll.append(5)
omnll.print_list()
print(return_middle_node(omnll).value)

emnll = LinkedList(1); emnll.append(2); emnll.append(3); emnll.append(4); emnll.append(5); emnll.append(6)
emnll.print_list()
print(return_middle_node(emnll).value)


print("---------------------Test Midde Node-----------------------------------------------")
print(has_loop(omnll))
print(has_loop(emnll))

print("---------------------Test Kth Node from the last-----------------------------------")
emnll.print_list()
omnll.print_list()

print(k_th_from_end(emnll, 3).value)
print(k_th_from_end(omnll, 1).value)

print("---------------------Test Removing Duplicates_______________________________________")
omnll = LinkedList(1); omnll.append(2); omnll.append(3); omnll.append(4); omnll.append(5)
omnll.append(2); omnll.append(3); omnll.append(4); omnll.append(5)
omnll.print_list()
remove_duplicates(omnll)
omnll.print_list()

print("------------------Test Binary to Decimal--------------------------------------------")
binr = LinkedList(1); binr.append(0);binr.append(1);binr.append(1);binr.append(1);
binr.print_list()
print(binary_to_decimal(binr))

print("------------------Test Partition--------------------------------------------")
binr = LinkedList(1); binr.append(3);binr.append(5);binr.append(7);binr.append(10);binr.append(52);binr.append(77);binr.append(16);
binr.print_list()
newll = partition_list(binr, 17)
newll.print_list()


print("--------------------Test Reverse By Range-----------------------------------")
binr = LinkedList(1); binr.append(3);binr.append(5);binr.append(7);binr.append(10);binr.append(52);binr.append(77);binr.append(16);
binr.print_list()
start = 1; end = 5; print(f"start:{start}, end:{end}")
newll = reverse_between(binr, start, end)
newll.print_list()

start = 0; end = 7; print(f"start:{start}, end:{end}")
newll = reverse_between(binr, start, end)
newll.print_list()

print("--------------------Test Swap By Pairs-----------------------------------")
binr = LinkedList(1); binr.append(3);binr.append(5);binr.append(7);binr.append(10);binr.append(52);binr.append(77);binr.append(16);
binr.print_list()
newll = swap_pairs(binr)
newll.print_list()

