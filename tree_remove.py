from tree_search import find_min

def remove_node(node, value):
    if node is None:
        return node
    
    if value < node.value:
        node.left = remove_node(node.left, value)
    elif value > node.value:
        node.right = remove_node(node.right, value)

    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        temp = find_min(node.right)
        node.value = temp.value
        node.right = remove_node(node.right, temp.value)
    
    return node

def remove_elements(root, values_to_remove):
    for val in values_to_remove:
        root = remove_node(root, val)
    return root