class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t = defaultdict(int)
        
        for i in range(n):
            t[i] = 0
        
        for a, b in trust:
            t[a - 1] -= 1
            t[b - 1] += 1
                
        for k, _ in t.items():
            if t[k] == n - 1:
                return k + 1
        return -1


# input: 
# 2
# [[1,2]]
# 3
# [[1,3],[2,3]]
# 3
# [[1,3],[2,3],[3,1]]
# 4
# [[1,3],[1,4],[2,3],[2,4],[4,3]]
# 3
# [[1,2],[2,3]]


# defaultdict(<class 'list'>, {0: -1, 1: 1})
# defaultdict(<class 'list'>, {0: -1, 1: -1, 2: 2})
# defaultdict(<class 'list'>, {0: 0, 1: -1, 2: 1})
# defaultdict(<class 'list'>, {0: -2, 1: -2, 2: 3, 3: 1})
# defaultdict(<class 'list'>, {0: -1, 1: 0, 2: 1})

# output:
# 2
# 3
# -1
# 3
# -1


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * n
        
        for a, b in trust:
            indegree[a - 1] -= 1
            indegree[b - 1] += 1

        for i, t in enumerate(indegree):
            if t == n - 1:
                return i + 1
        
        return -1