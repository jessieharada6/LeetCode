# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(l, r):
            trees = []
            if l > r:
                trees.append(None)
            
            for v in range(l, r + 1):
                left = dfs(l, v - 1)
                right = dfs(v + 1, r)
                
                for _l in left:
                    for _r in right:
                        root = TreeNode(v)
                        root.left = _l
                        root.right = _r
                        trees.append(root)
            return trees
    
        return dfs(1, n)