# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, targetSum, path, ans):
            if node is None: return
 
            targetSum -= node.val
            path.append(node.val)

            if node.left is node.right and targetSum == 0:
                ans.append([x for x in path])
                path.pop()
                return
            
            dfs(node.left, targetSum, path, ans)
            dfs(node.right, targetSum, path, ans)
            targetSum += node.val
            path.pop()

        dfs(root, targetSum, [], ans)
        return ans