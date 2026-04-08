class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

# ------------------------------------ BST ----------------------------------- #
def insert_bst(root, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = insert_bst(root.left, value)
    
    else:
        root.right = insert_bst(root.right, value)
    
    return root

def build_bst(values):
    root = None

    for val in values:
        root = insert_bst(root, val)

    return root

# ------------------------------------ AVL ----------------------------------- #
def build_avl_halving(sorted_values):
    if not sorted_values:
        return None

    mid = len(sorted_values) // 2
    root = Node(sorted_values[mid])

    root.left = build_avl_halving(sorted_values[:mid])
    root.right = build_avl_halving(sorted_values[mid+1:])

    return root

def build_avl(values):
    return build_avl_halving(sorted(values))