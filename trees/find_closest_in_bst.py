def findClosestValueInBst(tree, target):
    close = None
    return closestvalue(tree, target, close)

def closestValue(tree, target, close):
    if tree is None:
        return close
    if distance(target, close) > distance(target, tree.value):
        close = tree.value
    if target < tree.value:
        return closestValue(tree.left, target, close)
    elif target > tree.value:
        return closestValue(tree.right, target, close)
    else:
        return close

# distance between two numbers
def distance(a, b):
    return abs(a - b)
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
