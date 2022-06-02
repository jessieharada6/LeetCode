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
            if d > dist[cur]:  # can't get to another node
                continue
            
            for nei, cost in graph[cur]:
                if dist[cur] + cost < dist[nei]:
                    dist[nei] = dist[cur] + cost
                    heapq.heappush(heap, (dist[nei], nei))
        
        # print(dist)
        # min time to go to all nodes = max time to reach a node
        res = max(dist)
        return res if res != INF else -1