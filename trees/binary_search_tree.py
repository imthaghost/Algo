class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return True if self.left is None and self.right is None else False

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return True if self.left is not None or self.right is not None else False

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        O(n) traverse all nodes to find the longest path"""
        if self.left is None and self.right is None:
            return 0

        left_height = 0
        right_height = 0

        if self.left is not None:
            left_height = self.left.height()
        if self.right is not None:
            right_height = self.right.height()

        return max(left_height, right_height) + 1


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        O(n) traverse all nodes to find the longest path"""
        if root is not None:
            return root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        O(1) item we are looking for is the root node.
        O(h) where h is the height of the tree - longest path"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        O(1) Where the item we are looking for is at the root.
        O(h)  where h is the height of the tree - longest path"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        O(1) We are inserting at the root
        O(h)  where h is the height of the tree - longest path"""
        # if the tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        if item < parent.data:
            parent.left = BinaryTreeNode(item)
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        O(1) The item we are looking for is at the root.
        O(h)  where h is the height of the tree - longest path"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data:
                # Return the found node
                return node
            elif item < node.data:
                node = node.left
            elif item > node.data:
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        O(1) The item is at the root.
        O(h) With H being the height of the BST, we would have to loop to the height of the tree."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        elif item == node.data:
            # Return the found node
            return node
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        O(1) The item is at the root.
        O(h) With H being the height of the BST, we would have to loop to the height of the tree."""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data:
                # Return the parent of the found node
                return parent
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion).
        O(1) The item is at the root.
        O(h) With H being the height of the BST, we would have to loop to the height of the tree."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        O(1) The item is at the root.
        O(n * v) With H being the height of the BST, we would have to loop to the height of the tree."""
        return self._delete_helper(self.root, item)

    def _delete_helper(self, node, item):
        if node is None:
            return None

        if item < node.data:
            node.left = self._delete_helper(node, item)
        elif item > node.data:
            node.right = self._delete_helper(node, item)
        else:
            if node.left is None:
                tmp_node = node.right
                node = None
                return tmp_node
            elif node.right is None:
                tmp_node = node.left
                node = None
                return tmp_node

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        O(n * v) because we need to visit every item in the BST"""
        if node.left:
            self._traverse_in_order_recursive(node.left, visit)
        visit(node.data)
        if node.right:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        O(n * v) because we need to look through every item in the BST
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        O(n) because we need to look through every item in the BST
        TODO: Memory usage: ??? Why and under what conditions?"""

        visit(node.data)
        if node.left:
            self._traverse_pre_order_recursive(node.left, visit)
        if node.right:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        O(n) because we need to look through every item in the BST
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        O(n) because we need to look through every item in the BST
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node.left:
            self._traverse_post_order_recursive(node.left, visit)
        if node.right:
            self._traverse_post_order_recursive(node.right, visit)
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        O(n) because we need to look through every item in the BST
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        O(n) because we need to look through every item in the BST
        """
        queue = Queue()
        queue.enqueue(start_node)
        while not queue.is_empty():
            node = queue.dequeue()
            visit(node.data)
            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()