# Kruskal
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):              # current point
            for j in range(i + 1, n):   # next point
                xi = points[i][0]
                yi = points[i][1]
                xj = points[j][0]
                yj = points[j][1]
                edges.append([i, j, abs(xi - xj) + abs(yi - yj)])
        
        edges.sort(key=lambda x: x[2])
        
        mst = 0
        uf = UF(n)
        
        for e1, e2, cost in edges:
            if uf.connected(e1, e2):
                continue
            mst += cost
            uf.union(e1, e2)
            
        return mst

class UF:
    def __init__(self, n):
        self.c = n
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP == rootQ:
            return
        
        self.parent[rootP] = rootQ
        self.c -= 1
    
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        return rootP == rootQ
    
    def count(self):
        return self.c

# Prim
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
                                    # to build a MST, start somewhere
                                    # using weight as the sorting point, so can't put coordinates first
        vertices = [(0, (0, 0))]    # cost, (from, to) - starting from 0, 0 to 0 has cost of 0
        visited = set()             # add point if visited
        n = len(points)
        ans = 0
        
        while len(visited) < n:
            print(vertices, visited)
            c, (f, t) = heapq.heappop(vertices)
            if t in visited:
                continue
            
            ans += c
            visited.add(t)
            
            for node in range(n):
                if node not in visited:
                    heapq.heappush(vertices, (manhattan(points[t], points[node]), (t, node)))
                    
        return ans


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        vertices = [(0, (0, 0))]          
        visited = set()
        n = len(points)
        ans = 0
        
        while len(visited) < n:
            # print(vertices, visited)
            c, (f, t) = heapq.heappop(vertices)
            if t in visited:
                continue
            
            ans += c
            visited.add(t)
            
            for new_t in range(n):
                if new_t not in visited:
                    heapq.heappush(vertices, (manhattan(points[t], points[new_t]), (t, new_t)))
        return ans
                    

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        n = len(points)
        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                cost = manhattan(points[i], points[j])          # use cost to make heap
                graph[i].append((cost, j))
                graph[j].append((cost, i))
        
        # print(graph[0])
        ans, visited, heap = 0, set(), graph[0]
        
        visited.add(0)
        heapq.heapify(heap)

        while len(visited) < n:
            cost, to = heapq.heappop(heap)
            
            if to in visited:
                continue
            
            visited.add(to)
            ans += cost
            
            for new_to in graph[to]:
                if new_to not in visited:
                    heapq.heappush(heap, new_to)

        return ans
                    