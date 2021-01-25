# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def insert(self, value):
        currentNode = self
        while True:
            # if the value is less than the current node
            if value < currentNode.value:
                # if the current nodes left pointer is empty
                if currentNode.left is None:
                    # we can assign the left pointer of the current node to the value
                    currentNode.left = BST(value)
                    break
                else:
                    # otherwise we continue down the left side
                    currentNode = currentNode.left
            # if the value is greater then the current node        
            else:
                # if the current nodes right pointer is empty
                if currentNode.right is None:
                    # we can assign the right pointer of the current node to the value
                    currentNode.right = BST(value)
                    break
                else:
                    # otherwise we continue down the right side
                    currentNode = currentNode.right
        return self

        # Write your code here.
        # Do not edit the return statement of this method.
        return self
        
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def contains(self, value):
        # Write your code here.
        currentNode = self
        # while there are still values in tree
        while currentNode is not None:
            # if the value is less than the current node we search left
            if value < currentNode.value:
                currentNode = currentNode.left
            # if the value is greater than the current node we search right
            elif value > currentNode.value:
                currentNode = currentNode.right
            # the node is found
            else:
                return True
        return False           
                
            

    def remove(self, value, parentNode = None):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:

