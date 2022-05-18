class Solution:
    def numTrees(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[0] = 1
        nums[1] = 1
        
        for node in range(2, n + 1):                        #nodes
            for r in range(1, node + 1):                    #root val for each node
                nums[node] += nums[r - 1] * nums[node - r]  # l * r
        
        return nums[n]


class Solution:
    def __init__(self):
        self.cache = defaultdict(int)
        
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        if n in self.cache:                     # check cache
            return self.cache[n]
        
        count = 0
        for root in range(1, n + 1):            # where it repeats, use cache to avoid repeating calculation
            left = self.numTrees(root - 1)
            right = self.numTrees(n - root)
            count += left * right
        self.cache[n] = count
        
        return count


#------------------------------------------------------------------------------------------------#

class Solution:
    def numTrees(self, n: int) -> int:
        # when node is 0, there should be 0 tree
        # but we make it as 1 for multiplication
        t = [1 for _ in range(n + 1)]
        
        for nodes in range(2, len(t)):          # nodes
            total = 0
            for root in range(1, nodes + 1):    # root can not be 0, starting from 1
                left = t[root - 1]
                right = t[nodes - root]
                total += left * right           # sum
            t[nodes] = total                    # assign sum
       
        return t[-1]

class Solution:
    def __init__(self):
        self.cache = defaultdict(int)   # use cache to store n >= 2
        # self.cache[0] = 1
        # self.cache[1] = 1
    
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:            # when node is 1 or 2
            return 1
        
        if n in self.cache:
            return self.cache[n]
        
        count = 0
        for root in range(1, n + 1):    # where it repeats, as we go from [1, n] everytime
            l = self.numTrees(root - 1)
            r = self.numTrees(n - root)
            count += l * r
        self.cache[n] = count
        
        print(self.cache, count)
        return count                    # essential to return count, so num is accumulated
            

class Solution:
    def numTrees(self, n: int) -> int:
        t = 0
        nums = [1] * (n + 1)                    # base case 0, and 1 are both 1 for calculations below at s
        if n == 1:
            return 1
        
        for nodes in range(2, n + 1):           # starting from 2 as 1 is calculated
            s = 0
            for root in range(1, nodes + 1):    # starting from 1 as the lowest values of l and r is 1
                l = root - 1                    
                r = nodes - root
                s += nums[l] * nums[r]
            nums[nodes] = s       
        
        return nums[-1]   