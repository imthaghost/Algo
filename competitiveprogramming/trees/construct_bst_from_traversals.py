# A binary tree node 
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""Recursive function to construct binary of size len from
   Inorder traversal in[] and Preorder traversal pre[].  Initial values
   of inStrt and inEnd should be 0 and len -1.  The function doesn't
   do any error checking for cases where inorder and preorder
   do not form a tree """
def buildTree(inorder, preorder, start, end):
    # check if the the start is greater than the end
    if start > end:
        return None

    
    
    
1) Pick an element from Preorder. Increment a Preorder Index Variable (preIndex in below code) to pick next element in next recursive call. 
2) Create a new tree node tNode with the data as picked element. 
3) Find the picked element’s index in Inorder. Let the index be inIndex. 
4) Call buildTree for elements before inIndex and make the built tree as left subtree of tNode. 
5) Call buildTree for elements after inIndex and make the built tree as right subtree of tNode. 
6) return tNode.
Thanks to Rohini and Tushar for suggesting the code. 