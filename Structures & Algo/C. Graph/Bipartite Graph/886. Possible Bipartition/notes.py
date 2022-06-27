class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def buildGraph():
            graph = defaultdict(list)
            for edge in dislikes:
                w = edge[0]
                v = edge[1]
                graph[w].append(v)
                graph[v].append(w)
            return graph
                
        visited = [False for _ in range(n + 1)]
        color = [False for _ in range(n + 1)]
        ok = True
        graph = buildGraph()
        
        def traverse(node):
            nonlocal ok
            if not ok: return
            
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    color[nei] = not color[node]
                    traverse(nei)
                else:
                    if color[node] == color[nei]:
                        ok = False
        
        for i in range(1, n + 1):
            if not visited[i]:
                traverse(i)
        return ok

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.buildGraph(dislikes)
        
        color = [False for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
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

        
        for i in range(1, n + 1):
            if not visited[i]:
                traverse(i)
        return ok
    
    def buildGraph(self, dislikes):
        graph = defaultdict(list)
        for n in dislikes:
            node = n[0] 
            dislike = n[1] 
            # note: two directions
            graph[node].append(dislike)
            graph[dislike].append(node)
        return graph

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.buildGraph(dislikes)
        
        color = [False for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
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

        
        for i in range(1, n + 1):
            if not visited[i]:
                traverse(i)
        return ok
    
    def buildGraph(self, dislikes):
        graph = defaultdict(list)
        for n in dislikes:
            node = n[0] 
            dislike = n[1] 
            # note: two directions
            graph[node].append(dislike)
            graph[dislike].append(node)
        return graph