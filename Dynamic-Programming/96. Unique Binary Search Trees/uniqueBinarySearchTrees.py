class Solution:
    def numTrees(self, n: int) -> int:
        # base case 
        # 0 nodes = 1 tree
        # 1 node = 1 tree
        dp = [1] * (n + 1)
        
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                # recursion not needed
                # looking at number of nodes from 2
                # then to 3, and so on
                left = dp[root - 1]
                right = dp[nodes - root]
                total += left * right
            # when we have x number of nodes
            # number of tree we can build
            dp[nodes] = total
        
        return dp[n]              