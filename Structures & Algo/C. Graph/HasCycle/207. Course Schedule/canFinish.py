class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = [False for _ in range(numCourses)]    # all nodes will be visited in the end, avoid revisit
        onPath = [False for _ in range(numCourses)]     # where the snake body is at at the moment
        hasCycle = False
        
        def traverse(node):
            nonlocal hasCycle
            if onPath[node]:
                hasCycle = True                         # snake head bites itself
                return
            if visited[node] or hasCycle:
                return

            visited[node] = True
            onPath[node] = True
            
            for n in graph[node]:
                traverse(n)
            onPath[node] = False
               
        for k in range(numCourses):                     # as it is not all connected, must traverse the list
            traverse(k)
        return not hasCycle


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        indegree = [0 for _ in range(numCourses)]
        for a, b in prerequisites:                      # a: to, b: from, a dependes on b
            indegree[a] += 1
        # print(graph, indegree)
        
        q = []
        for i in range(numCourses):
            if indegree[i] == 0:                        # indegree[i] = 0: no dependent ndoe
                q.append(i)
        
        count = 0
        while q:
            cur = q.pop(0)
            count += 1
            for n in graph[cur]:
                indegree[n] -= 1
                if indegree[n] == 0:                    # all dependent node is traversed
                    q.append(n)
        
        return count == numCourses
            
            