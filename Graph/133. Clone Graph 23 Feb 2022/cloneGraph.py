"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# BFS & HashMap
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        # oldNode: newlyCreatedNode
        m = {node: Node(node.val)}
        
        queue = deque([node])
        
        while queue:
            n = queue.popleft()
            
            for nei in n.neighbors:
                if nei not in m:
                    queue.append(nei)
                    # create a new node
                    m[nei] = Node(nei.val)
                # append the nei to current node
                m[n].neighbors.append(m[nei])
        
        return m[node]


# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        m = {}
        
        def dfs(node):
            if node in m:
                return m[node]
            
            m[node] = Node(node.val)
            
            for nei in node.neighbors:
                m[node].neighbors.append(dfs(nei))
            
            #.popleft()
            return m[node]
        
        dfs(node)
        return m[node]

                
    
    