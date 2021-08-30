class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prerequesites list   
        pre_map = { i:[] for i in range(numCourses) }
        # add prerequsit to the map 
        for course, prerequisite in prerequisites:
            pre_map[course].append(prerequisite)
        
        # print(pre_map)
        
        # all courses along the current DFS path
        visitSet = set()
        # check based on each course, using numCourses
        def dfs(course):
            if course in visitSet:
                return False
            if pre_map[course] == []:
                return True
            
            # add course       
            visitSet.add(course)

            # check pre on each course
            # course (key) -> pre (value)  
            for pre in pre_map[course]:
                # if no loop in the pre, this will not run
                # visit pre 
                if not dfs(pre): return False
            
            # if the for above never runs
            # clear the course in the set, and map
            # note, pre is still in the set
            visitSet.remove(course)
            pre_map[course] = []
            return True
        
        # for the graph that is not fully connected
        # they will not call each other based on the pre
        # 1->2, 3->4
        for course in range(numCourses):
            if not dfs(course): return False
        return True
        