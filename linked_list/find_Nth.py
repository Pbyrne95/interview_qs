from Node_class import Node 

def nth_from_last(head, n):
    if not head:
        return None

    curr = head
    pos = 0 
    depth = 0

    while curr:
        if curr.value == n:
            pos = depth
        curr = curr.child
        depth += 1

    return  depth - pos if pos else None

    
    
current = Node(1)
for i in range(2, 8):
    current = Node(i, current)

head = current

current2 = Node(4)
for i in range(3, 0, -1):
    current2 = Node(i, current2)
head2 = current2

print(nth_from_last(head, 1))  
print(nth_from_last(head, 5)) 
print(nth_from_last(head2, 2))
print(nth_from_last(head2, 4))
print(nth_from_last(head2, 5))
print(nth_from_last(None, 1)) 
