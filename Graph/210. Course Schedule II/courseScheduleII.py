class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list of papers 
        pre_map = { c:[] for c in range(numCourses)}
        for [course, pre] in prerequisites:
            pre_map[course].append(pre)
            
        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs has been added to output, but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visited, cycle = set(), set()
        
        def dfs(course):
            # detect cycle
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            # iterate pre in each course
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output
            