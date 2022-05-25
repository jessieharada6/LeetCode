class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False for _ in range(n)]
        color = [False for _ in range(n)]
        ok = True
        
        def traverse(node):
            nonlocal ok
            if not ok: return
            
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:            # base case if visited[nei]: return
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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False for _ in range(n)]
        color = [False for _ in range(n)]
        ok = True
        
        def traverse(node):
            nonlocal ok
            q = []
            visited[node] = True
            q.append(node)
            
            while ok and q:
                n = q.pop()
                for nei in graph[n]:
                    if not visited[nei]:
                        color[nei] = not color[n]
                        visited[nei] = True
                        q.append(nei)
                    else:
                        if color[nei] == color[n]:
                            ok = False
                            
         
        for i in range(n):
            if not visited[i]:
                traverse(i)
        return ok