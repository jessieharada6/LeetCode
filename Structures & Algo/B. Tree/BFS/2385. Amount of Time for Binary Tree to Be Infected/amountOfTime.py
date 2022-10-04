# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {}
        def dfs(node, pa):
            if not node: return
            if node.val == start:
                self.start = node
                
            parents[node] = pa
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        
        ans = -1
        q = [self.start]
        visit = {self.start, None}
        while q:
            ans += 1
            tmp = q
            q = []
            for node in tmp:
                for x in node.left, node.right, parents[node]:
                    if x not in visit:
                        visit.add(x)
                        q.append(x)
        return ans