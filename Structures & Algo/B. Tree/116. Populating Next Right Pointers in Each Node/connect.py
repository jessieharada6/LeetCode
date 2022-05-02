"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        def connectTwo(node1, node2):
            if node1 is None or node2 is None:
                return
            
            # connect
            node1.next = node2
            
            # same node
            connectTwo(node1.left, node1.right)
            connectTwo(node2.left, node2.right)
            
            # different nodes
            connectTwo(node1.right, node2.left)
        
        
         # "Initially, all next pointers are set to NULL."
        connectTwo(root.left, root.right)

        return root