def leaf_BST(self):
    self._leafHelper(self.root)
    print()


def _leafHelper(self, node):
    if node:
        self._leafHelper(node.left)
        # Leaf: no left and no right child
        if node.left is None and node.right is None:
            print(node.element, end=" ")
        self._leafHelper(node.right)


# Print all non-leaf (internal) nodes (in-order)
def non_leaf_BST(self):
    self._nonleafHelper(self.root)
    print()


def _nonleafHelper(self, node):
    if node:
        self._nonleafHelper(node.left)
        # Non-leaf: has at least one child
        if node.left is not None or node.right is not None:
            print(node.element, end=" ")
        self._nonleafHelper(node.right)


def total_nodesBST(self, node):
    """
    Performs a pre-order walk of the subtree rooted at `node`, prints each element,
    and returns the total count of nodes in that subtree.
    """
    count = self._totalNodesHelper(node)
    print()  # newline after node listing
    print("Total nodes:", count)
    return count

def _totalNodesHelper(self, node):
    if node is None:
        return 0
    # visit this node
    print(node.element, end=" ")
    # count this node + children
    left_count = self._totalNodesHelper(node.left)
    right_count = self._totalNodesHelper(node.right)
    return 1 + left_count + right_count

    def depth_nodeBST(self, node):
        depth = self._depthHelper(self.root, node, 0)
        if depth >= 0:
            print(f"Depth of node {node.element}: {depth}")
        else:
            print(f"Node {node.element} not found in tree.")
        return depth

    def _depthHelper(self, current, target, current_depth):
        if current is None:
            return -1
        if current is target:
            return current_depth
        # Choose subtree based on the target’s value relative to current
        if target.element < current.element:
            return self._depthHelper(current.left, target, current_depth + 1)
        else:
            return self._depthHelper(current.right, target, current_depth + 1)
