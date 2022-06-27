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


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False for _ in range(n)]
        color = [False for _ in range(n)]
        ok = True
        q = collections.deque()
        
        def traverse(node):
            nonlocal ok
            
            q.append(node)
            
            while ok and q:
                
                cur = q.popleft()
                visited[cur] = True

                for nei in graph[cur]:
                    if not visited[nei]:
                        q.append(nei)
                        visited[nei] = True
                        color[nei] = not color[cur]
                    else:
                        if color[nei] == color[cur]:
                            ok = False

        for i in range(n):
            if not visited[i]:
                traverse(i)
        
        return ok