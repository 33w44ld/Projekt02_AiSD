# -------------------------- Usuwanie całego drzewa -------------------------- #
def delete_post_order(node, deleted_nodes):
    if node is None:
        return
    
    delete_post_order(node.left, deleted_nodes)
    delete_post_order(node.right, deleted_nodes)
    deleted_nodes.append(node.value)

    node.left = None
    node.right = None

def delete_all(root):
    if root is None:
        print("Tree is empty")
        return None
    
    deleted_nodes = []
    delete_post_order(root, deleted_nodes)

    print(f"Deleting: {' '.join(map(str,deleted_nodes))}")
    print("Tree successfully removed")

    return None