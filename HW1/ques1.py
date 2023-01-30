class Node:
    def __init__(self, val=None):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

head1 = LinkedList()
head2 = LinkedList()

node_a = Node("a")
node_b = Node("b")
node_c = Node("c")
node_d = Node("d")
node_e = Node("e")
node_f = Node("f")
node_1 = Node("1")
node_2 = Node("2")

head1.head = node_a
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = node_f

head2.head = node_1
node_1.next = node_2
node_2.next = node_b  # Intersecting node

print("List 1")
head1.printlist()

print("\n\nList 2")
head2.printlist()

def intersectFinder(h1, h2):
    m = n = 0

    h1_x = h1
    h2_x = h2

    # Count the length of both the lists
    while not(h1 == None and h2 == None):
        if h1 != None:
            m += 1
            h1 = h1.next

        if h2 != None:
            n += 1
            h2 = h2.next 
    print("Length of List 1: {} \tList 2: {}".format(m, n))


    # Offsetting the list
    if m >=n:
        h1, h2 = h1_x, h2_x
    else:
        h1, h2 = h2_x, h1_x
    offset = abs(m - n)
    for i in range(offset):
        h1 = h1.next

    # Return the intersecting node
    while h1 != None:
        if h1 == h2:
            return h1
        h1 = h1.next
        h2 = h2.next
    return None

res_node = intersectFinder(head1.head, head2.head)

if res_node:
    print(res_node.data)
else:
    print("No intersection found!")