# BFS

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (x, y), z in zip(equations, values):
            graph[x][y] = z
            graph[y][x] = 1 / z
            
        result = []
        
        
        def dfs(src, dst):
            if not (src in graph or dst in graph):
                return -1.0
            
            queue = [(src, 1.0)]
            visited = set()
            
            for (x, v) in queue:
                if x == dst:
                    # return at this point
                    return v
                
                # add to set
                visited.add(x)
                
                # for key in dictionary
                for y in graph[x]:
                    if y not in visited:
                        queue.append((y, v * graph[x][y]))
            return -1.0
        
        for (x, y) in queries:
            result.append(dfs(x, y))
        return result

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (x, y), z in zip(equations, values):
            graph[x][y] = z
            graph[y][x] = 1/z
        
        print(dict(graph))
        
        def bfs(src, dst):
            if not (src in graph or dst in graph):
                return -1.0
            
            queue = [(src, 1.0)]
            visited = set()
            
            for x, val in queue:
                if x == dst:
                    return val
                visited.add(x)
                
                for y in graph[x]:
                    if y not in visited:
                        queue.append((y, val * graph[x][y]))
            return -1.0
        
        return [bfs(src, dst) for src, dst in queries]
                    
        
# NOTES
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # dict in defaultdict() describes the data type at value
        graph = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            # {x: {y: v}}
            graph[x][y] = v
            # {y: {x: v}}
            graph[y][x] = 1 / v
        
        print(dict(graph))
            
        def bfs(src, dst):
            if not (src in graph or dst in graph): 
                return -1.0
            
            # everytime when a new element from queries comes in
            # this is a new queue and a new set
            seen = set()
            queue = [(src, 1.0)]
            for x, val in queue:
                if x == dst:
                    # return the value to the final result
                    return val 
                seen.add(x)
                
                for y in graph[x]:
                    if y not in seen:
                        print(x, y)
                        queue.append((y, val*graph[x][y]))
                        print("====", queue)
            return -1.0

        # list comprehension
        return [bfs(src, dest) for src, dest in queries]


# DFS 
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (x, y), z in zip(equations, values):
            graph[x][y] = z
            graph[y][x] = 1 / z
            
        result = []
        
        def dfs(src, dst, visited):
            if not (src in graph or dst in graph):
                return -1.0
            
            for y in graph[src]:
                # print(y, dst)
                if y == dst:
                    return graph[src][dst]
            
            visited.add(src)
            
            for y in graph[src]:
                if not y in visited:
                    # for ["a", "b"], now "b" is y - aka: src
                    weight = dfs(y, dst, visited)
                    # print(weight, graph[src][y], y, dst)
                    if weight != -1.0:
                        return graph[src][y] * weight
            
            visited.remove(src);
            return -1.0
        
        for (x, y) in queries:
            visited = set()
            result.append(dfs(x, y, visited))
        return result

# Union find
# given query [a, b], if they share the same root, find out the value of common_root/a and common_root/b, then result if (common_root/a) / (common_root/b)

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        root_dict = {}
        result = []
        
        def find(node):
            parent_node, parent_val = root_dict.setdefault(node, (node, 1.0))
            if node != parent_node:
                root_node, root_val = find(parent_node)
                root_dict[node] = (root_node, root_val * parent_val)
            return root_dict[node]
        
        def union(x, y, ratio):
            x_root, x_val, y_root, y_val = *find(x), *find(y)
            
            if not ratio:
                # conclude finding/relationship btw 2 nodes with the same root
                return x_val / y_val if x_root == y_root else -1.0
            if x_root != y_root:
                # build graph
                root_dict[x_root] = (y_root, y_val / x_val * ratio)
                
        # build initial graph
        for (x, y), v in zip(equations, values):
            union(x, y, v)
        
        #update graph and add findings to result
        for (x, y) in queries:
            if x in root_dict and y in root_dict:
                result.append(union(x, y, 0))
            else:
                result.append(-1.0)
                
        return result
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        root = {}
        result = []
        
        def find(x):
            # if key already exist, returns value of a key
            # if not, insert
            # if it's a: (b:2.0)
            # then x is a, p is b, and xr is 2.0 
            p, xr = root.setdefault(x, (x, 1.0))
            print("find", x, p, xr)
            # x != p not the same root
            if x != p:
                r, pr = find(p)
                print("x!=p", x, p, r, xr, pr)
                root[x] = (r, xr * pr)
                print("root[x]", root[x])
            return root[x]
        
        def union(x, y, ratio):
            # find(x) returns ('a', 1.0)
            # *find(x) unpacks px and xr -> a and 1.0
            px, xr, py, yr = *find(x), *find(y)
            print("after", px, xr, py, yr)
            # if ratio == 0:
            if not ratio:
                # px === py means same root
                print("ratio", ratio, xr, yr)
                return xr / yr if px == py else -1.0
            if px != py:
                print("px != py", root[px])
                root[px] = (py, yr/xr*ratio)
        
        for (x, y), v in zip(equations, values):
            union(x, y, v)
        
        print(root)
        #{'a': ('b', 2.0), 'b': ('c', 3.0), 'c': ('c', 1.0)}
        for x, y in queries:
            if x in root and y in root:
                result.append(union(x, y, 0))
            else:
                result.append(-1.0)
        
        #return [union(x, y, 0) if x in root and y in root else -1.0 for x, y in queries]
        #print(root)
        #{'a': ('c', 6.0), 'b': ('c', 3.0), 'c': ('c', 1.0)}
        return result