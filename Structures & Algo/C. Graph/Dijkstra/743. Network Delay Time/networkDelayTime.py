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


## 