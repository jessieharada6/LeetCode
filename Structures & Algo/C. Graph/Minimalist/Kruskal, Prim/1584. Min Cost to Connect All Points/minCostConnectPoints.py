# Kruskal
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def m(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        n = len(points)
        edges = []
        for i in range(n):                      # current point
            for j in range(i + 1, n):           # next point
                edges.append((i, j, m(points[i], points[j])))
        
        edges.sort(key = lambda x : x[2])   # starting from the shortest distance by sorting based on cost ascendingly
        
        mst = 0
        uf = UF(n)
        for a, b, cost in edges:
            if uf.connect(a, b):             # can't connect if a, b alr have the same parent, will have cycle
                continue
            
            uf.union(a, b)                   # union a, b
            mst += cost                      # add cost
            
        return mst                           # if uf.count() == 1 else - 1

class UF:
    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP == rootQ:
            return
        
        self.parents[rootP] = rootQ
        self.count -= 1
    
    def connect(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        return rootP == rootQ
    
    def count(self):
        return self.count

# Prim
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def m(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        n = len(points)
        mst = 0
        visited = [False for _ in range(n)]
        
        heap = []
        heapq.heappush(heap, (0, (0, 0)))   # (cost, (from, to)): from 0 to 0, cost is 0
        
        while heap:
            c, (f, to) = heapq.heappop(heap)
            
            if visited[to]:
                continue
            
            visited[to] = True
            mst += c
            for node in range(n):
                if not visited[node]:   # only the nodes that have not been traversed
                                        ### to becomes new_from, node becomes new_to
                    heapq.heappush(heap, (m(points[node], points[to]), (to, node)))
            
        return mst