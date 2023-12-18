# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        @cache
        def dfs(node): #返回在当前节点最长的路径 （来自左路径或右路径） 不管当前节点下面怎么绕来绕去 取左或右的最大值
            nonlocal ans
            if node is None: return -1

            l = dfs(node.left) + 1
            r = dfs(node.right) + 1
            print(l, r, node.val)
            ans = max(ans, l + r)
            return max(l, r) # [3,1,null,null,2] get max when node 1's right child can be counted as 1 diameter
        dfs(root)
        return ans