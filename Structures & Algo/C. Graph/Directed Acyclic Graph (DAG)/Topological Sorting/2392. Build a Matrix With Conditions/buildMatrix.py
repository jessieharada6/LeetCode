class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            graph = [[] for _ in range(k)]
            indegree = [0] * k
            
            for x, y in edges:
                graph[x - 1].append(y - 1)
                indegree[y - 1] += 1
            
            q = collections.deque(i for i, v in enumerate(indegree) if v == 0)
            order = []
            
            while q:
                x = q.popleft()
                order.append(x)
                for y in graph[x]:
                    indegree[y] -= 1
                    if indegree[y] == 0:
                        q.append(y)
            
            return order if len(order) == k else None
        
        row = topo_sort(rowConditions)
        col = topo_sort(colConditions)
        if not row or not col:
            return []
        
        m = [[0] * k for _ in range(k)]
        for i in range(k):
            m[row.index(i)][col.index(i)] = i + 1
        
        return m