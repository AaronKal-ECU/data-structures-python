from typing import List, Optional
import sys
import math

# Data Structures Question 1 - Task 2
# Aaron Mark Kalaji, May 23 2025

class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def insert(self, key: int):
        if key < self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = Node(key)
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = Node(key)

def build_bst(sequence: List[int]) -> Node:
    root = Node(sequence[0])
    for value in sequence[1:]:
        root.insert(value)
    return root

def calculate_root_index(n: int) -> int:
    if n <= 1:
        return 0
    h = math.floor(math.log2(n))
    nodes_above = (1 << h) - 1
    last_count = n - nodes_above
    max_left_last = 1 << (h - 1)
    left_last = min(last_count, max_left_last)
    left_nodes = (1 << (h - 1)) - 1
    return left_nodes + left_last

def complete_BST_seq(sorted_array: List[int], output: List[int]):
    if not sorted_array:
        return
    n = len(sorted_array)
    root_index = calculate_root_index(n)
    output.append(sorted_array[root_index])
    complete_BST_seq(sorted_array[:root_index], output)
    complete_BST_seq(sorted_array[root_index + 1:], output)

# ------ Tree visualisation (Computing 101, March 4 2025) ------
class AsciiNode:
    left = None
    right = None
    edge_length = 0
    height = 0
    lablen = 0
    parent_dir = 0
    label = ''

MAX_HEIGHT = 1000
lprofile = [0] * MAX_HEIGHT
rprofile = [0] * MAX_HEIGHT
INFINITY = (1 << 20)
gap = 3

def build_ascii_tree_recursive(t: Optional[Node]) -> Optional[AsciiNode]:
    if t is None:
        return None
    node = AsciiNode()
    node.left = build_ascii_tree_recursive(t.left)
    node.right = build_ascii_tree_recursive(t.right)
    if node.left:
        node.left.parent_dir = -1
    if node.right:
        node.right.parent_dir = 1
    node.label = str(t.key)
    node.lablen = len(node.label)
    return node


def build_ascii_tree(t: Optional[Node]) -> Optional[AsciiNode]:
    if t is None:
        return None
    node = build_ascii_tree_recursive(t)
    node.parent_dir = 0
    return node


def compute_lprofile(node, x, y):
    if node is None:
        return
    isleft = (node.parent_dir == -1)
    lprofile[y] = min(lprofile[y], x - ((node.lablen - isleft) // 2))
    if node.left:
        for i in range(1, node.edge_length + 1):
            if y + i < MAX_HEIGHT:
                lprofile[y + i] = min(lprofile[y + i], x - i)
    compute_lprofile(node.left, x - node.edge_length - 1, y + node.edge_length + 1)
    compute_lprofile(node.right, x + node.edge_length + 1, y + node.edge_length + 1)


def compute_rprofile(node, x, y):
    if node is None:
        return
    notleft = (node.parent_dir != -1)
    rprofile[y] = max(rprofile[y], x + ((node.lablen - notleft) // 2))
    if node.right:
        for i in range(1, node.edge_length + 1):
            if y + i < MAX_HEIGHT:
                rprofile[y + i] = max(rprofile[y + i], x + i)
    compute_rprofile(node.left, x - node.edge_length - 1, y + node.edge_length + 1)
    compute_rprofile(node.right, x + node.edge_length + 1, y + node.edge_length + 1)


def compute_edge_lengths(node):
    if node is None:
        return
    compute_edge_lengths(node.left)
    compute_edge_lengths(node.right)
    if not node.left and not node.right:
        node.edge_length = 0
    else:
        if node.left:
            for i in range(min(node.left.height, MAX_HEIGHT)):
                rprofile[i] = -INFINITY
            compute_rprofile(node.left, 0, 0)
            hmin = node.left.height
        else:
            hmin = 0
        if node.right:
            for i in range(min(node.right.height, MAX_HEIGHT)):
                lprofile[i] = INFINITY
            compute_lprofile(node.right, 0, 0)
            hmin = min(node.right.height, hmin)
        delta = gap + 1
        for i in range(hmin):
            delta = max(delta, gap + 1 + rprofile[i] - lprofile[i])
        if ((node.left and node.left.height == 1) or (node.right and node.right.height == 1)) and delta > gap + 1:
            delta -= 1
        node.edge_length = ((delta + 1) // 2) - 1
    h = 1
    if node.left:
        h = max(node.left.height + node.edge_length + 1, h)
    if node.right:
        h = max(node.right.height + node.edge_length + 1, h)
    node.height = h

print_next = 0

def print_level(node, x, level):
    global print_next
    if node is None:
        return
    isleft = (node.parent_dir == -1)
    if level == 0:
        spaces = x - print_next - ((node.lablen - isleft) // 2)
        sys.stdout.write(' ' * spaces)
        print_next += spaces
        sys.stdout.write(node.label)
        print_next += node.lablen
    elif node.edge_length >= level:
        if node.left:
            spaces = x - print_next - level
            sys.stdout.write(' ' * spaces)
            print_next += spaces
            sys.stdout.write('/')
            print_next += 1
        if node.right:
            spaces = x - print_next + level
            sys.stdout.write(' ' * spaces)
            print_next += spaces
            sys.stdout.write('\\')
            print_next += 1
    else:
        print_level(node.left, x - node.edge_length - 1, level - node.edge_length - 1)
        print_level(node.right, x + node.edge_length + 1, level - node.edge_length - 1)


def drawTree(t: Optional[Node]):
    if t is None:
        return
    proot = build_ascii_tree(t)
    compute_edge_lengths(proot)
    for i in range(proot.height):
        lprofile[i] = INFINITY
    compute_lprofile(proot, 0, 0)
    xmin = min(lprofile[:proot.height])
    global print_next
    for level in range(proot.height):
        print_next = 0
        print_level(proot, -xmin, level)
        print()
    if proot.height >= MAX_HEIGHT:
        print(f"This tree is taller than {MAX_HEIGHT}, and may be drawn incorrectly.")

# ----- Main Execution -----

datasets = {
    "Test case 1": [19, 1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 2, 18, 90, 122, 132, 0, 66, 100, 12, 17],
    "Test case 2": [7, 7, 8, 8, 10, 10, 5, 5, 1, 2],
    "Test case 3": [-7, -333, -8, -15, 2, -4, -6],
}

for name, data in datasets.items():
    print(f"{name} (Complete BST):")
    print("Original sequence:", data)
    sorted_data = sorted(data)
    print("Sorted sequence:  ", sorted_data)
    rearranged: List[int] = []
    complete_BST_seq(sorted_data, rearranged)
    print("Re-arranged sequence for complete BST:", rearranged)
    bst_root = build_bst(rearranged)
    print("BST visualization (complete):")
    drawTree(bst_root)
    print("\n" + "=" * 50 + "\n")
