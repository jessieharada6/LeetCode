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