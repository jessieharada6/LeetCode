class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for e in flights:
            graph[e[1]].append((e[0], e[2]))
        
        k += 1
        memo = [[-2] * (k + 1) for _ in range(n)]
        
        def dp(s, k):
            if s == src: return 0
            if k == 0: return -1
            res = math.inf
            
            if memo[s][k] != -2: return memo[s][k]

            for (f, c) in graph[s]:
                sub = dp(f, k - 1)
                if sub != -1:
                    res = min(res, sub + c)
            
            res = -1 if res == math.inf else res
            memo[s][k] = res
            return res
        
        return dp(dst, k)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[t].append((f, p))
        # print(graph)
        k += 1
        memo = [[-2] * (k + 1) for _ in range(n)]
        
        def dp(s, k):
            if s == src: return 0
            if k == 0: return -1
            res = math.inf
            if memo[s][k] != -2: return memo[s][k]
            
            for (f, price) in graph[s]:
                sub = dp(f, k - 1)
                if sub != -1:
                    res = min(res, sub + price)
                # print(s, f, res)
            memo[s][k] = res
            return res
        
        res = dp(dst, k) 
        return res if res != math.inf else -1


# Dijkstra
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, path in flights:
            graph[s].append((d, path))
        
        k += 1
        heap = []
        heapq.heappush(heap, (0, src, k))
        
        vis = [0] * n
        
        while heap:
            d, cur, k = heapq.heappop(heap)
            if cur == dst: return d
            if vis[cur] >= k: continue
            vis[cur] = k
            for nei, cost in graph[cur]:
                heapq.heappush(heap, (d + cost, nei, k - 1))
        
        # print(dist)
        return -1