
# zigzag 特性 左右左右
# isLeft 用传参和前序保留 之前的方向 与即将进行的走向比较
# cur 记录当前路径长度
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, isLeft, cur):  # 至上而下 前序 
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

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        # 返回的是从 node 出发的，向左走的最长长度，向右走的最长长度
        def dfs(node): # 至下而上 后序 返回 往上
            if node is None: return -1, -1
            
            left_len = dfs(node.left)[1] + 1 # 即将向左,拿目前向右走的最长长度
            right_len = dfs(node.right)[0] + 1

            nonlocal ans
            ans = max(ans, left_len, right_len) # 543: left_len + right_len 路径 = 从 node 出发往左走的最长长度 + 从 node 出发往右走的最长长度
            return left_len, right_len
        
        dfs(root)
        return ans