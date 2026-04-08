from trees import Node
import math

def rotate_right(parent, node):
    child = node.left
    node.left = child.right
    child.right = node
    parent.right = child

def rotate_left(parent, node):
    child = node.right
    node.right = child.left
    child.left = node
    parent.right = child

def dsw_rebalance(root):
    if root is None:
        return None
    
    dummy = Node(0)
    dummy.right = root
    
    # ---------------------------- FAZA 1: Prostowanie --------------------------- #
    parent = dummy
    curr = dummy.right
    count = 0
    while curr:
        if curr.left:
            rotate_right(parent, curr)
            curr = parent.right
        else:
            count += 1
            parent = curr
            curr = curr.right
    
    # ---------------------------- FAZA 2: Zwijanie --------------------------- #
    h = int(math.log2(count + 1))
    m = 2**h - 1
    
    perform_rotations(dummy, count - m)
    
    while m > 1:
        m //= 2
        perform_rotations(dummy, m)
        
    return dummy.right

def perform_rotations(root_parent, count):
    curr = root_parent.right
    parent = root_parent
    for _ in range(count):
        if curr and curr.right:
            rotate_left(parent, curr)
            parent = parent.right
            curr = parent.right