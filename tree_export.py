def generate_tikz(node):
    if node is None:
        return ""
    
    if node.left is None and node.right is None:
        return f"node {{{node.value}}}"
    
    l_str = f"child {{{generate_tikz(node.left)}}}" if node.left  else "child[missing]"
    r_str = f"child {{{generate_tikz(node.right)}}}" if node.right  else "child[missing]"

    return f"node {{{node.value}}} \n {l_str} \n {r_str}"

def export_tree(root):
    if root is None:
        print("Drzewo jest puste, brak danych do eksportu")
        return
    
    tikz_code = generate_tikz(root)
    final_output = f"\\{tikz_code};"
    print(final_output)