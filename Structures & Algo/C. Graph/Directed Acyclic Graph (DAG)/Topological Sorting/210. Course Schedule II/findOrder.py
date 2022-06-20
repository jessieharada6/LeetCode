class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        onPath = [False for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        hasCycle = False
        postOrder = []
        
        def traverse(node):
            nonlocal hasCycle
            if onPath[node]:
                hasCycle = True                # check cycle
                return
            if visited[node] or hasCycle:
                return
            
            visited[node] = True
            onPath[node] = True
            for n in graph[node]:
                traverse(n)
            postOrder.append(node)              # append all child tasks, then parent task
            onPath[node] = False
        
        for i in range(numCourses):
            traverse(i)
        
        if hasCycle:
            return []
        
        return postOrder[::-1]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        indegree = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            indegree[a] += 1
        
        queue = []
        order = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            cur = queue.pop()    # when dependent node is 0 and points to 2 diff nodes, the orders won't matter          
                                 # [[1,0],[2,0],[3,1],[3,2]] -> [0, 2, 1, 3] or [0, 1, 2, 3] both ok
            order.append(cur)
            count += 1
            for n in graph[cur]:
                indegree[n] -= 1
                if indegree[n] == 0:    # avoid cycle, similar to visited in dfs
                    queue.append(n)
        
        return order if count == numCourses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        onPath = [False for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        hasCycle = False
        courses = []
        
        def traverse(node):
            nonlocal hasCycle 
            if onPath[node]:
                hasCycle = True
                return
            if visited[node] or hasCycle:
                return
            
            onPath[node] = True
            visited[node] = True
            # print("pre", node)              # similar to root, left, right, so orders not guaranteed
            for n in graph[node]:
                traverse(n)
            # print("post", node)             # similar to left, right, root, so order is reversed
            courses.append(node)
            onPath[node] = False
        
        for i in range(numCourses):
            traverse(i)
        # print(courses)
        if hasCycle:
            return []
        return courses[::-1]
                