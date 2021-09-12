class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # edge case
        if n == 1:
            return [0]
        
        # record graph and degree
        outupt = []
        map = { i: [] for i in range(n) }
        degree = [0 for _ in range(n) ]
        
        for a, b in edges:
            map[a].append(b)
            map[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        print(map, degree)
        
        queue = [ i for i, e in enumerate(degree) if e == 1]
        #print(queue)
        
        # traverse using size of queue
        # queue only contains degree of 1
        # refresh list 
        while len(queue):
            list = []
            size = len(queue)
            for _ in range(size):
                current = queue.pop(0)
                list.append(current)
                for n in map[current]:
                    degree[n] -= 1
                    if degree[n] == 1:
                        queue.append(n)
            outupt = list
            
        return outupt