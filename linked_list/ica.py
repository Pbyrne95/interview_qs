class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    # Overriding the equality operator.
    # This will be used for testing your solution.
    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False

def node_search(top,target):

    def add_to_list(elem,lis):
        if elem not in lis:
            lis.append(elem)
        return lis
         
    seen = [top.value]
    top_left = top
    found = False
    while top_left.left and top_left.right and not found:
        if (top_left.left.value == target):
            seen.append(top_left.left.value)
            found = True
            
        if(top_left.right.value == target):
            seen.append(top_left.left.value)
            found = True

        add_to_list(top_left.left.value,seen)
        add_to_list(top_left.right.value,seen)
        top_left = top_left.left
    return seen if seen else None

def get_list(curr_n,elem):
    if elem in node_search(curr_n.right,elem):
        return node_search(curr_n.right,elem)
    elif elem in node_search(curr_n.left,elem):
        return node_search(curr_n.left,elem)
    else:
        return None

def lca(head,attr1,attr2):
    if attr1 == attr2:
        return attr1
    if head.value == attr1 or head.value == attr2:
        return head.value

    head_val = head.value
    list_one = get_list(head,attr1)
    list_two = get_list(head,attr2)

    if list_one and list_two:
        merged_list = list(set(list_one).intersection(list_two))
        return Node(min(merged_list)).value if merged_list else head_val

def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head

mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
head1 = create_tree(mapping1, 0)
mapping2 = {5: [1, 4], 1: [3, 8], 4: [9, 2], 3: [6, 7]}
head2 = create_tree(mapping2, 5)


print(lca(head1, 1, 5)) #should return 0
print(lca(head1, 3, 1)) #should return 1
print(lca(head1, 1, 4)) #should return 1
print(lca(head1, 0, 5)) #should return 0
print(lca(head2, 4, 7)) #should return 5
print(lca(head2, 3, 3)) #should return 3
print(lca(head2, 8, 7)) #should return 1
print(lca(head2, 3, 0)) #should return None (0 does not exist in the tree)