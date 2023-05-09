# Implement the depth FirstSearch method on the Node class. This method receives an empty array, traverses the tree 
# from left to right using the Depth-first Search methodology, puts all of the nodes' names in the input array, and then returns the array.

# A Node class with a name and an array of optional child nodes is provided to you. Nodes combine to create an acyclic tree-like structure.
# Sample Input

# graph = A
#          /  |  \
#         B   C   D
#        / \     / \
#       E   F   G   H
#          / \   \
#         I   J   K
    

# Sample Output

# ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
    

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name) # Add current node's name to the array
        for child in self.children:
            child.depthFirstSearch(array) # Recursively call DFS on each child node
        return array
    
# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V) where V is the number of vertices
