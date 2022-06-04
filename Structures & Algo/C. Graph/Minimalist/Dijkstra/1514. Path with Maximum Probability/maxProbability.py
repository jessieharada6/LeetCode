class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for ((e1, e2), cost) in zip(edges, succProb): # nodes to each other
            graph[e1].append((e2, cost))
            graph[e2].append((e1, cost))
        # print(graph)
        
        heap = []
        heapq.heappush(heap, (1, start))
        
        dist = [-math.inf for _ in range(n)]                # getting max so fill in -math.inf
        dist[start] = 1                                     # note: the possibility from start to start is 1
        
        while heap:
            c, cur = heapq.heappop(heap)
            
            for nei, d in graph[cur]:
                # print(cur, nei, d)
                if dist[cur] * d > dist[nei]:               # get max 
                    dist[nei] = dist[cur] * d
                    heapq.heappush(heap, (-dist[nei], nei)) # turn min heap to max heap but dist doesn't change
        # print(dist)
        return dist[end] if dist[end] != -math.inf else 0        