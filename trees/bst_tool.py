import math
import sys

# Data Structures Question 2 - Full Program
# Aaron Mark Kalaji, May 23 2025

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def createNewNode(self, e):
        return TreeNode(e)

    def search(self, e):
        current = self.root
        while current:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                return True
        return False

    def find_node(self, key):
        current = self.root
        while current:
            if key < current.element:
                current = current.left
            elif key > current.element:
                current = current.right
            else:
                return current
        return None

    def insert(self, e):
        if self.search(e):
            return False
        if self.root is None:
            self.root = self.createNewNode(e)
        else:
            parent = None
            current = self.root
            while current:
                parent = current
                if e < current.element:
                    current = current.left
                else:
                    current = current.right
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)
        self.size += 1
        return True

    def inorder(self):
        self._inorder_helper(self.root)
        print()
    def _inorder_helper(self, node):
        if node:
            self._inorder_helper(node.left)
            print(node.element, end=' ')
            self._inorder_helper(node.right)

    def preorder(self):
        self._preorder_helper(self.root)
        print()
    def _preorder_helper(self, node):
        if node:
            print(node.element, end=' ')
            self._preorder_helper(node.left)
            self._preorder_helper(node.right)

    def postorder(self):
        self._postorder_helper(self.root)
        print()
    def _postorder_helper(self, node):
        if node:
            self._postorder_helper(node.left)
            self._postorder_helper(node.right)
            print(node.element, end=' ')

    def inverse_inorder(self):
        self._inverse_inorder_helper(self.root)
        print()
    def _inverse_inorder_helper(self, node):
        if node:
            self._inverse_inorder_helper(node.right)
            print(node.element, end=' ')
            self._inverse_inorder_helper(node.left)

    def leaf_BST(self):
        self._leaf_helper(self.root)
        print()
    def _leaf_helper(self, node):
        if node:
            self._leaf_helper(node.left)
            if not node.left and not node.right:
                print(node.element, end=' ')
            self._leaf_helper(node.right)

    def non_leaf_BST(self):
        self._nonleaf_helper(self.root)
        print()
    def _nonleaf_helper(self, node):
        if node:
            self._nonleaf_helper(node.left)
            if node.left or node.right:
                print(node.element, end=' ')
            self._nonleaf_helper(node.right)

    def total_nodesBST(self, node):
        count = self._total_nodes_helper(node)
        print(f"\nTotal nodes: {count}")
        return count
    def _total_nodes_helper(self, node):
        if not node:
            return 0
        print(node.element, end=' ')
        left_count = self._total_nodes_helper(node.left)
        right_count = self._total_nodes_helper(node.right)
        return 1 + left_count + right_count

    def depth_nodeBST(self, N):
        depth = self._depth_helper(self.root, N, 0)
        if depth >= 0:
            print(f"Depth of node {N.element}: {depth}")
        else:
            print(f"ERROR: Node {N.element} not found!")
        return depth
    def _depth_helper(self, current, target, depth):
        if current is None:
            return -1
        if current is target:
            return depth
        if target.element < current.element:
            return self._depth_helper(current.left, target, depth + 1)
        return self._depth_helper(current.right, target, depth + 1)

    def depth_subtreeBST(self, N):
        height = self._subtree_height_helper(N)
        print(f"Depth of subtree rooted at {N.element}: {height}")
        return height
    def _subtree_height_helper(self, node):
        if node is None:
            return 0
        left_h = self._subtree_height_helper(node.left)
        right_h = self._subtree_height_helper(node.right)
        return 1 + max(left_h, right_h)

    def delete_node(self, key):
        if not self.search(key):
            return False
        self.root, _ = self._delete_helper(self.root, key)
        self.size -= 1
        return True

    def _delete_helper(self, node, key):
        if key < node.element:
            node.left, _ = self._delete_helper(node.left, key)
            return node, True
        elif key > node.element:
            node.right, _ = self._delete_helper(node.right, key)
            return node, True
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True
        successor = self._find_min(node.right)
        node.element = successor.element
        node.right, _ = self._delete_helper(node.right, successor.element)
        return node, True

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_list(self):
        arr = []
        self._inorder_list_helper(self.root, arr)
        return arr
    def _inorder_list_helper(self, node, arr):
        if node:
            self._inorder_list_helper(node.left, arr)
            arr.append(node.element)
            self._inorder_list_helper(node.right, arr)

    def to_balanced(self):
        arr = self.inorder_list()
        self.clear()
        def build_balanced(a):
            if not a:
                return None
            mid = len(a) // 2
            node = self.createNewNode(a[mid])
            node.left = build_balanced(a[:mid])
            node.right = build_balanced(a[mid+1:])
            return node
        self.root = build_balanced(arr)
        self.size = len(arr)

    def to_complete(self):
        arr = self.inorder_list()
        self.clear()
        def build_complete(a):
            n = len(a)
            if n == 0:
                return None
            if n == 1:
                return self.createNewNode(a[0])
            h = math.floor(math.log2(n))
            nodes_above = (1 << h) - 1
            last_count = n - nodes_above
            max_left_last = 1 << (h - 1)
            left_last = min(last_count, max_left_last)
            left_nodes = (1 << (h - 1)) - 1
            root_idx = left_nodes + left_last
            node = self.createNewNode(a[root_idx])
            node.left = build_complete(a[:root_idx])
            node.right = build_complete(a[root_idx+1:])
            return node
        self.root = build_complete(arr)
        self.size = len(arr)

    def display_tree(self, node=None, level=0):
        if self.root is None:
            print("(empty tree)")
            return
        if node is None:
            node = self.root
        if node.right:
            self.display_tree(node.right, level+1)
        print("    " * level + str(node.element))
        if node.left:
            self.display_tree(node.left, level+1)

    def isEmpty(self):
        return self.size == 0

    def clear(self):
        self.root = None
        self.size = 0


def level1_menu():
    preset = [67, 93, 77, 32, 47, 91, 35, 26, 33, 115, 104, 57, 97, 63, 59, 60, 62, 58, 3, -7]
    while True:
        print("\nLevel-1 Menu:")
        print("1. Load preset sequence")
        print("2. Manually enter keys")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")
        tree = BST()
        if choice == '1':
            for x in preset:
                tree.insert(x)
            break
        elif choice == '2':
            print("Enter integers one by one (blank to finish):")
            while True:
                val = input()
                if val == '':
                    break
                try:
                    tree.insert(int(val))
                except ValueError:
                    pass
            break
        elif choice == '3':
            print("Exiting program...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
    level2_menu(tree)


def level2_menu(tree):
    while True:
        print("\nLevel-2 Menu:")
        print("1. Display tree shape and traversals")
        print("2. Display all leaf and non-leaf nodes")
        print("3. Display a subtree and count its nodes")
        print("4. Display depth of a given node")
        print("5. Display depth of a subtree")
        print("6. Insert a new integer key")
        print("7. Delete an integer key")
        print("8. Convert to balanced BST")
        print("9. Convert to complete BST")
        print("10. End program")
        choice = input("Enter choice (1-10): ")

        if choice == '1':
            print("\nTree shape:")
            tree.display_tree()
            print("Pre-order:", end=' '); tree.preorder()
            print("In-order :",end=' '); tree.inorder()
            print("Post-order:",end=' '); tree.postorder()

        elif choice == '2':
            print("\nLeaves: ",end=''); tree.leaf_BST()
            print("Non-leaves: ",end=''); tree.non_leaf_BST()

        elif choice == '3':
            key = int(input("Enter subtree root key: "))
            node = tree.find_node(key)
            if node:
                print(f"\nSubtree shape rooted at {key}:")
                tree.display_tree(node)
                tree.total_nodesBST(node)
            else:
                print(f"ERROR: Node {key} not found!")

        elif choice == '4':
            key = int(input("Enter node key: "))
            node = tree.find_node(key)
            if node:
                tree.depth_nodeBST(node)
            else:
                print(f"ERROR: Node {key} not found!")

        elif choice == '5':
            key = int(input("Enter subtree root key: "))
            node = tree.find_node(key)
            if node:
                tree.depth_subtreeBST(node)
            else:
                print(f"ERROR: Subtree rooted at node {key} not found!")

        elif choice == '6':
            key = int(input("Enter key to insert: "))
            if not tree.insert(key):
                print(f"ERROR: node key {key} already exists in the BST!")
            else:
                print("Inserted.")
                print("Inverse-in-order:",end=' '); tree.inverse_inorder()

        elif choice == '7':
            key = int(input("Enter key to delete: "))
            if not tree.delete_node(key):
                print(f"ERROR: Node {key} not found!")
            else:
                print("Deleted.")
                print("Updated tree shape:")
                tree.display_tree()

        elif choice == '8':
            tree.to_balanced()
            print("Tree converted to balanced BST:")
            tree.display_tree()

        elif choice == '9':
            tree.to_complete()
            print("Tree converted to complete BST:")
            tree.display_tree()

        elif choice == '10':
            print("Exiting program...")
            sys.exit(0)

        else:
            print("Invalid choice. Please enter a number 1-10.")

if __name__ == '__main__':
    level1_menu()