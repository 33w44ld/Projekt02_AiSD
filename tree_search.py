# --------------------------- Wyszukiwanie Min/Max --------------------------- #
def find_min(node):
    if node is None:
        return None
    current = node
    while current.left is not None:
        current = current.left
    return current

def find_max(node):
    if node is None:
        return None
    current = node
    while current.right is not None:
        current = current.right
    return current

# ---------------------------- Wypisywanie Min/Max --------------------------- #

def find_min_max(root):
    min_node = find_min(root)
    max_node = find_max(root)

    if min_node and max_node:
        print(f"Min: {min_node.value}")
        print(f"Max: {max_node.value}")
    else:
        print("Tree is empty")