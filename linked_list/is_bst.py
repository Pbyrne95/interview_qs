class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

def is_bst(node, lower_lim=None, upper_lim=None):
    head_node = node.value
    search_node = node

    search_left = search_node.left
    if search_left.value > head_node:
        return False
    while search_left.left or search_left.right:
        if(search_left.value < head_node):
            
            previous = search_left.value
            left_val = search_left.left.value
            right_val = search_left.right.value

            if((left_val > head_node or previous < left_val ) or \
                (right_val > head_node or right_val < previous )):
                return False
        else:
            return False
        search_left = search_left.left

    search_right = search_node.right 

    while search_right.left and search_right.right:
        if(search_right.value > head_node):
            previous = search_right.value
            
            left_val = search_right.left.value
            right_val = search_right.right.value
       
            if( (left_val < head_node or previous < left_val ) or \
                (right_val < head_node or right_val < previous ) ):
                return False
        else:
            return False
        search_right = search_right.right

    return True

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

mapping0 = {0: [1, 2]}
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
mapping4 = {3: [1, 5], 1: [0, 4]}

print(is_bst(create_tree(mapping0,0)))
print(is_bst(create_tree(mapping1,0)))
print(is_bst(create_tree(mapping2,3)))
print(is_bst(create_tree(mapping3,3)))
print(is_bst(create_tree(mapping4,3)))


