# Create a program that takes an input of integer value and a Binary Search Tree (BST) and returns the BST value that is the closest match to the target value.

# Note: There will only be one closest value, so you can assume that.

# Each BST node has a left child node, a right child node, and an integer value. 
# If and only if a node satisfies the following conditions, it is said to be a valid BST node: its value strictly exceeds the values of every node to its left; 
# its value strictly undercuts or equals the values of every node to its right; and its children's nodes are either valid BST nodes themselves or None / null.

# Sample Input

# tree =   10
#            /     \
#           5      15
#         /   \   /   \
#        2     5 13   22
#      /           \
#     1            14
#     target = 12
    

# Sample Output

# 13
def findClosestValueInBst(tree, target):
    # Write your code here.
    closest = tree.value
    curr_node = tree
    
    while curr_node is not None:
        if abs(target - curr_node.value) < abs(target - closest):
            closest = curr_node.value
        
        if target < curr_node.value:
            curr_node = curr_node.left
        elif target > curr_node.value:
            curr_node = curr_node.right
        else:
            break
    
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
