"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 将孩子节点两两相连
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return root
        def dfs(node1, node2):
            if node1 is None or node2 is None: return None

            node1.next = node2
            dfs(node1.left, node1.right) 
            dfs(node1.right, node2.left) 
            dfs(node2.left, node2.right)

        dfs(root.left, root.right)
        return root

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

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        if root.left is not None:                            # connect nodes under the same root
            root.left.next = root.right
        if root.right is not None and root.next is not None: # connect nodes under different roots
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        
        return root