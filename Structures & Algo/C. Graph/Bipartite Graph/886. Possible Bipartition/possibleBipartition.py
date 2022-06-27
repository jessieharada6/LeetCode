class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        visited = [False for _ in range(n)]
        color = [False for _ in range(n)]
        ok = True
        
        def traverse(node):
            nonlocal ok
            if not ok: return
            
            visited[node] = True
            
            for nei in graph[node]:
                if not visited[nei]:
                    color[nei] = not color[node]
                    traverse(nei)
                else:
                    if color[nei] == color[node]:
                        ok = False
        
        for i in range(n):
            if not visited[i]:
                traverse(i)
        
        return ok

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        # print(graph)
        
        visited = [False for _ in range(n)]
        color = [False for _ in range(n)]
        ok = True
        
        def traverse(node):
            nonlocal ok
            q = collections.deque()
            q.append(node)
            visited[node] = True
            
            while q and ok:
                cur = q.popleft()
                
                for nei in graph[cur]:
                    if not visited[nei]:
                        color[nei] = not color[cur]
                        visited[nei] = True 
                        q.append(nei)
                    else:
                        if color[nei] == color[cur]:
                            ok = False
        
        for i in range(n):
            if not visited[i]:
                traverse(i)
        
        return ok