"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node', map = {}) -> 'Node':
        if not node:
            return None
        
        if node in map:
            return map[node]
        
        # copy is the cloned node
        # it is an entry point of all nodes and neighbors
        copy = Node(node.val)
        # the only function of map is to record visited node
        map[node] = copy
        
        for n in node.neighbors:
            # update copy's neighbors 
            copy.neighbors.append(self.cloneGraph(n, map))
            
        return copy


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node', map = {}) -> 'Node':
        if not node:
            return None
        
        map[node] = Node(node.val)
        queue = []
        queue.append(node)
        
        while len(queue):
            current = queue.pop(0)
            for n in current.neighbors:
                if n not in map:
                    # record a new node
                    map[n] = Node(n.val)
                    # add to queue
                    queue.append(n)
                # two nodes connect with each other
                map[n].neighbors.append(map.get(current))
                
        return map[node]