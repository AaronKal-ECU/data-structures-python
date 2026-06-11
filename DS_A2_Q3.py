import sys

# Data Structures Question 3 - AVL Tree Program
# Aaron KALAJI 10670705, May 23 2025

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0
        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def insert(self, key):
        if self.node is None:
            self.node = Node(key)
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < self.node.key:
            self.node.left.insert(key)
        elif key > self.node.key:
            self.node.right.insert(key)
        self._rebalance()

    def delete_AVLNode(self, key):
        if self.node is None:
            return False
        deleted = False
        if key < self.node.key:
            deleted = self.node.left.delete_AVLNode(key)
        elif key > self.node.key:
            deleted = self.node.right.delete_AVLNode(key)
        else:
            deleted = True
            if self.node.left.node is None and self.node.right.node is None:
                self.node = None
                return True
            if self.node.left.node is None:
                self.node = self.node.right.node
                return True
            if self.node.right.node is None:
                self.node = self.node.left.node
                return True
            succ = self.node.right._min_node()
            self.node.key = succ.key
            self.node.right.delete_AVLNode(succ.key)
        if deleted:
            self._rebalance()
        return deleted

    def _min_node(self):
        curr = self.node
        while curr.left.node is not None:
            curr = curr.left.node
        return curr

    def _update_metrics(self):
        if self.node is None:
            self.height = -1
            self.balance = 0
        else:
            self.node.left._update_metrics()
            self.node.right._update_metrics()
            lh = self.node.left.height
            rh = self.node.right.height
            self.height = max(lh, rh) + 1
            self.balance = lh - rh

    def _rebalance(self):
        self._update_metrics()
        if self.balance > 1:
            if self.node.left.balance < 0:
                self.node.left._rotate_left()
            self._rotate_right()
            self._update_metrics()
        if self.balance < -1:
            if self.node.right.balance > 0:
                self.node.right._rotate_right()
            self._rotate_left()
            self._update_metrics()

    def _rotate_left(self):
        A = self.node
        B = A.right.node
        T = B.left.node
        self.node = B
        B.left.node = A
        A.right.node = T

    def _rotate_right(self):
        A = self.node
        B = A.left.node
        T = B.right.node
        self.node = B
        B.right.node = A
        A.left.node = T

    def inorder_traverse(self):
        if self.node is None:
            return []
        return (self.node.left.inorder_traverse() +
                [self.node.key] +
                self.node.right.inorder_traverse())

    def preorder_traverse(self):
        if self.node is None:
            return []
        return ([self.node.key] +
                self.node.left.preorder_traverse() +
                self.node.right.preorder_traverse())

    def postorder_traverse(self):
        if self.node is None:
            return []
        return (self.node.left.postorder_traverse() +
                self.node.right.postorder_traverse() +
                [self.node.key])

    def display(self, level=0, pref='Root'):
        self._update_metrics()
        if self.node is not None:
            print('  ' * level + f"{pref}: {self.node.key} [h={self.height} b={self.balance}]")
            self.node.left.display(level+1, 'L')
            self.node.right.display(level+1, 'R')

def count_nodes_by_depth(self):
    counts = {}
    def recurse(tree, d):
        if tree.node is None:
            return
        counts[d] = counts.get(d, 0) + 1
        recurse(tree.node.left, d+1)
        recurse(tree.node.right, d+1)
    recurse(self, 0)
    return counts

def get_leaf_nodes(self):
    leaves = []
    def recurse(tree):
        if tree.node is None:
            return
        if tree.node.left.node is None and tree.node.right.node is None:
            leaves.append(tree.node.key)
        else:
            recurse(tree.node.left)
            recurse(tree.node.right)
    recurse(self)
    return leaves

def get_non_leaf_nodes(self):
    non_leaves = []
    def recurse(tree):
        if tree.node is None:
            return
        if not (tree.node.left.node is None and tree.node.right.node is None):
            non_leaves.append(tree.node.key)
        recurse(tree.node.left)
        recurse(tree.node.right)
    recurse(self)
    return non_leaves

AVLTree.count_nodes_by_depth = count_nodes_by_depth
AVLTree.get_leaf_nodes = get_leaf_nodes
AVLTree.get_non_leaf_nodes = get_non_leaf_nodes

PRESET_LIST = [55, 79, -31, 18, 40, 75, 29, 5, -1, -4, 95, 93, 43, 84, 53, 46, 47, 48, 44, 74, 90]

def build_tree_from_preset():
    print("Building AVL tree from preset list...")
    return AVLTree(PRESET_LIST)

def manual_build_tree():
    tree = AVLTree()
    print("Enter integer keys one by one. Press Enter on blank line to finish.")
    while True:
        s = input("Key: ").strip()
        if s == '':
            break
        try:
            tree.insert(int(s))
        except ValueError:
            print("Invalid integer, try again.")
    return tree


def level2_menu(tree):
    while True:
        print("\n-- AVL Operations --")
        print("1. Display AVL tree")
        print("2. Show traversals (pre/in/post)")
        print("3. Print leaf & non-leaf nodes")
        print("4. Insert a key")
        print("5. Delete a key")
        print("6. Show statistics by depth")
        print("7. Return to main menu")
        choice = input("Choice> ").strip()
        if choice == '1':
            tree.display()
        elif choice == '2':
            print("Pre-order:", tree.preorder_traverse())
            print("In-order :", tree.inorder_traverse())
            print("Post-order:", tree.postorder_traverse())
        elif choice == '3':
            print("Leaf nodes    :", tree.get_leaf_nodes())
            print("Non-leaf nodes:", tree.get_non_leaf_nodes())
        elif choice == '4':
            try:
                k = int(input("Insert key> "))
                tree.insert(k)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            try:
                k = int(input("Delete key> "))
                if not tree.delete_AVLNode(k):
                    print("Key not found.")
            except ValueError:
                print("Invalid input.")
        elif choice == '6':
            counts = tree.count_nodes_by_depth()
            max_d = max(counts.keys())
            print("\nStatistics Table:")
            print(f"{'Depth':>5} | {'Count':>5}")
            print("------|------")
            for d in range(max_d+1):
                print(f"{d:>5} | {counts.get(d,0):>5}")
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

def main():
    while True:
        print("\n== AVL Tree Builder ==")
        print("1. Pre-load preset sequence")
        print("2. Manually enter keys")
        print("3. Exit")
        choice = input("Select> ").strip()
        if choice == '1':
            tree = build_tree_from_preset()
            level2_menu(tree)
        elif choice == '2':
            tree = manual_build_tree()
            level2_menu(tree)
        elif choice == '3':
            sys.exit(0)
        else:
            print("Invalid selection.")

if __name__ == '__main__':
    main()
