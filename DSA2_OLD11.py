from typing import List, Optional

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

def balanced_BST_seq(sorted_array: List[int], output: List[int]):
    if not sorted_array:
        return
    n = len(sorted_array)
    mid = n // 2 if n % 2 == 0 else (n - 1) // 2
    output.append(sorted_array[mid])
    balanced_BST_seq(sorted_array[:mid], output)
    balanced_BST_seq(sorted_array[mid + 1:], output)

def display_tree(node: Optional[Node], level: int = 0):
    if not node:
        return
    display_tree(node.right, level + 1)
    print('    ' * level + str(node.key))
    display_tree(node.left, level + 1)

datasets = {
    "Dataset 1": [19, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 2, 18, 90, 122, 132, 0, 66, 100, -12, 17],
    "Dataset 2": [7, 3, 8, 5, 2, 4, 6, 4, 1, 1],
    "Dataset 3": [7, 333, 8, 15, 2, -4, 6],
}

for name, data in datasets.items():
    print(f"{name}:")
    print("Original sequence:", data)
    sorted_data = sorted(data)
    print("Sorted sequence:  ", sorted_data)
    rearranged = []
    balanced_BST_seq(sorted_data, rearranged)
    print("Re-arranged seq:  ", rearranged)
    bst_root = build_bst(rearranged)
    print("BST visualization:")
    display_tree(bst_root)
    print("\n" + "=" * 50 + "\n")