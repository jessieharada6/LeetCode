class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * 100
        colours = [False] * 100
        
        queue = []
        
        for i in range(len(graph)):
            if len(graph[i]) == 0 or visited[i] == True:
                continue
            
            queue.append(i)
            visited[i] = True
            colours[i] = True

            while len(queue) != 0:
                node = queue.pop(0)
                for nei in graph[node]:
                    if visited[nei] == False:
                        queue.append(nei)
                        # mark nei as visited
                        visited[nei] = True
                        # colour of nei should be the opposite
                        # to the colour of node
                        colours[nei] = not colours[node]
                    elif colours[node] == colours[nei]:
                        return False
        return True