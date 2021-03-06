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
        visited = set()                 # don't need to add 0 before the while loop, as it will never reach the for loop
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
        def m(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                cost = m(points[i], points[j])      # use cost to make heap
                graph[i].append((cost, j))          # nodes to each other
                graph[j].append((cost, i))          # nodes to each other
                
        
        # print(graph)
        
        mst = 0
        heap = graph[0]                             # a random point
        heapq.heapify(heap)
        visited = set()
        visited.add(0)                              # mark what's in the heap as visited as it is nodes to each other, if mark inside the loop, some nodes can never be reached and lead to while true loop
        
        while len(visited) < n:
            cost, to = heapq.heappop(heap)
            
            if to in visited:
                continue
            
            mst += cost
            visited.add(to)
            
            for c, new_to in graph[to]:
                if new_to not in visited:
                    heapq.heappush(heap, (c, new_to))
        
        return mst