import time
import statistics
import sys
import csv
from trees import build_bst, build_avl
from tree_rebalance import dsw_rebalance
from tree_search import find_min, find_max
from tree_print import inOrder

sys.setrecursionlimit(100000)

def measure_execution(func, *args):
    times = []
    for _ in range(4):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        times.append(end - start)
    return statistics.mean(times)

def run_benchmark():
    sizes = [1024, 2048, 4096, 8192, 16384, 32768]
    filename = "wyniki_benchmark.csv"
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["n", "BST_Create", "AVL_Create", "Search_MinMax", "InOrder", "DSW_Rebalance"])
        
        for n in sizes:
            data = list(range(n))
            
            t_bst = measure_execution(build_bst, data)
            t_avl = measure_execution(build_avl, data)
            
            curr_bst = build_bst(data)
            curr_avl = build_avl(data)
            
            t_search = measure_execution(lambda: (find_min(curr_avl), find_max(curr_avl)))
            t_inorder = measure_execution(inOrder, curr_avl, [])
            t_dsw = measure_execution(dsw_rebalance, curr_bst)
            
            writer.writerow([n, f"{t_bst:.6f}", f"{t_avl:.6f}", f"{t_search:.6f}", f"{t_inorder:.6f}", f"{t_dsw:.6f}"])

if __name__ == "__main__":
    run_benchmark()