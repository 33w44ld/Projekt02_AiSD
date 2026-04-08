import argparse
import sys

from trees import build_bst, build_avl

def print_help():
    print("Help \tShow this message")
    print("Print \tPrint the tree (in-order, pre-order, post-order)")
    print("Remove \tRemove elements of the tree")
    print("Delete \tDelete whole tree")
    print("Export \tExport the tree to tikzpicture")
    print("Rebalance \tRebalance the tree")
    print("Exit \tExits the program (same as Ctrl+D)")
