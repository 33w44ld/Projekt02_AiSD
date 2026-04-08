# ------------------------------ In-Order ------------------------------ #
def inOrder(node, res):
    if node is None:
        return
    inOrder(node.left, res)
    res.append(node.value)
    inOrder(node.right, res)

# ------------------------------ Pre-Order ----------------------------- #
def preOrder(node, res):
    if node is None:
        return
    res.append(node.value)
    preOrder(node.left, res)
    preOrder(node.right, res)

# -------------------------------- Post-Order -------------------------------- #
def postOrder(node, res):
    if node is None:
        return
    postOrder(node.left, res)
    postOrder(node.right, res)
    res.append(node.value)


# -------------------------------- Print Tree -------------------------------- #
def print_tree(root):
    res_in = []
    inOrder(root, res_in)
    print("In-order: ", ", ".join(map(str, res_in)))

    res_pre = []
    preOrder(root, res_pre)
    print("Pre-order: ", ", ".join(map(str, res_pre)))

    res_post = []
    postOrder(root, res_post)
    print("Post-order: ", ", ".join(map(str, res_post)))