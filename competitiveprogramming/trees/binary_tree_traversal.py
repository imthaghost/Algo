def inOrderTraverse(tree, array):
    # check to see if tree has values
    if tree is not None:
        # traverse to left node
        inOrderTraverse(tree.left, array)
        # append the left most node
        array.append(tree.value)
        # traverse right
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    # Write your code here.
    if tree is not None:
        # root node
        array.append(tree.value)
        # left 
        preOrderTraverse(tree.left)
        preOrderTraverse(tree.right) 
    return array


def postOrderTraverse(tree, array):
    # Write your code here.
    if tree is not None:
        postOrderTraverse(tree.left)
        postOrderTraverse(tree.right)
        array.append(tree.value)
    return array

