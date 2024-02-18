
# zigzag 特性 左右左右
# isLeft 用传参和前序保留 之前的方向 与即将进行的走向比较
# cur 记录当前路径长度
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, isLeft, cur):
            if node is None: return

            nonlocal ans
            ans = max(ans, cur)
            
            if isLeft: # prev
                dfs(node.left, True, 1)
                dfs(node.right, False, cur + 1)
            else:
                dfs(node.left, True, cur + 1)
                dfs(node.right, False, 1)
        
        dfs(root, False, 0)
        return ans