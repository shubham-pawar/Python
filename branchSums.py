# Create a program that takes a binary tree as an input and outputs a list of its branch sums in the leftmost to rightmost order

# The total of all values in a Binary Tree branch is known as the branch sum. A path of nodes in a tree that begins at the root node and 
# ends at any leaf node is known as a binary tree branch.

# Each Binary Tree node has a left child node, a right child node, and an integer value. Children nodes may either be additional Binary Tree nodes 
# or None or null.

# Sample Input

# tree =     1
#             /     \
#            2       3
#          /   \    /  \
#         4     5  6    7
#       /   \  /
#      8    9 10
    

# Sample Output

# [15, 16, 18, 10, 11]
#      15 == 1 + 2 + 4 + 8
#      16 == 1 + 2 + 4 + 9
#      18 == 1 + 2 + 5 + 10
#      10 == 1 + 3 + 6
#      11 == 1 + 3 + 7
    

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
    
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)