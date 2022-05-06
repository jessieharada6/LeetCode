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