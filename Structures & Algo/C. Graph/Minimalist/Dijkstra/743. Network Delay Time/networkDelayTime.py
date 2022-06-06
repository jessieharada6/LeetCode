## Dijkstra
## positive distance due to the data strcuture used - heap
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = math.inf
        graph = defaultdict(list)
        for edge in times:
            f = edge[0] - 1
            t = edge[1] - 1
            cost = edge[2]
            graph[f].append((t, cost))
        # print(graph)
        
        dist = [INF for _ in range(n)]              # initially, all dist is inf
        
        start = k - 1
        dist[start] = 0                             # update dist from start to start 
        
        heap = []
        heapq.heappush(heap, (0, start))
        
        while heap:
            d, cur = heapq.heappop(heap)
            if d > dist[cur]:  
                continue
            
            for nei, cost in graph[cur]:
                if dist[cur] + cost < dist[nei]:
                    dist[nei] = dist[cur] + cost
                    heapq.heappush(heap, (dist[nei], nei))              # add the updated distance with the node to heap
        
        # print(dist)
        # min time to go to all nodes = max time to reach a node
        res = max(dist)
        return res if res != INF else -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for edge in times:
            graph[edge[0] - 1].append((edge[1] - 1, edge[2]))
        
        dist = [math.inf for _ in range(n)]
        dist[k - 1] = 0
        heap = []
        heapq.heappush(heap, (0, k - 1))

        while heap:
            d, cur = heapq.heappop(heap)
            if dist[cur] < d:
                continue
            
            for nei, c in graph[cur]:
                if dist[cur] + c < dist[nei]:
                    dist[nei] = dist[cur] + c
                    heapq.heappush(heap, (dist[nei], nei))  # add the updated distance with the node to heap
        
        
        return max(dist) if max(dist) != math.inf else -1


## spfa - Shortest Path Faster Algorithm - Bellman Ford 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for e in times:
            edges[e[0] - 1].append((e[1] - 1, e[2]))       # with direction
        print(edges)
        dist = [math.inf for _ in range(n)]
        start = k - 1
        dist[start] = 0
        
        # visited = set()
        
        q = collections.deque()
        q.append(start)
        
        while q:
            cur = q.popleft()
            print(cur)
            
            # if cur in visited:              # preventing from being revisited,                                           #     continue                    # rquired for graph with no directions
            # visited.add(cur)
            
            for nei, d in edges[cur]:
                if dist[cur] + d < dist[nei]:
                    dist[nei] = dist[cur] + d
                    q.append(nei)
            print(q, dist)
  
        ans = max(dist)                                      # min time for all nodes to receive the signal
        return ans if ans != math.inf else -1

# Floyd
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[math.inf for _ in range(n)] for _ in range(n)]
        for col, row, cost in times:
            edges[col - 1][row - 1] = cost
        
        for i in range(n):
            edges[i][i] = 0
        # print(edges)
        
        for start in range(n):
            # print(start)
            for x in range(n):
                for y in range(n):
                    # [1][3] = [1][2] + [2][3] 
                    edges[x][y] = min(edges[x][y], edges[x][start] + edges[start][y]) 
                    # print(x, start, y, edges[x][y])
        # print(edges)
        return max(edges[k - 1]) if max(edges[k - 1]) != math.inf else -1