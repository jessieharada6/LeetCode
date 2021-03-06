class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False for _ in range(n)]
        color = [False for _ in range(n)]
        ok = True
        
        def traverse(node):
            nonlocal ok
            if not ok: return

            # if visited[index]:
            #     return
            
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
            q = collections.deque()
            q.append(node)
            visited[node] = True
            
            while ok and q:
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