
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        path = []
        
        def traverse(node):
            path.append(node)
            
            if node == len(graph) - 1:
                paths.append(path[:])               # path shallow copy - path[:]
                return
            
            for n in graph[node]:
                traverse(n)
                path.pop()
                
        
        traverse(0)                                 # define starting point e.g. from node 0 to node n - 1 so starting point is 0
        return paths

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        path = [0]
        
        def traverse(node):
            # print("node", node)   # it will have the root value
            if node == len(graph) - 1:
                paths.append(path[:])
                return
            
            for n in graph[node]:   # in the for loop, it won't have the root value
                path.append(n)
                # print("before n", n)
                traverse(n)
                # print("after n", n)
                path.pop()
                
        
        traverse(0)
        return paths

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        path = []
        def traverse(node):
            path.append(node)
            
            if node == len(graph) - 1:
                paths.append(path[:])
                path.pop()
                return
            
            for n in graph[node]: 
                traverse(n)
                
            path.pop() 
        
        traverse(0)             
        return paths