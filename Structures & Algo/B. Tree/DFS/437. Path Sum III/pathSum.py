# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        path = collections.defaultdict(int)
        path[0] = 1
        def dfs(node, targetSum, psum, path):
            if node is None: return 

            psum += node.val
            
            # print(psum, path)
            nonlocal ans
            if targetSum == 0:
                ans += path[psum]
            else:
                ans += path[psum - targetSum] # i < j保证非空子数组 不可用同一个数相减(i == j)
            
            path[psum] += 1
            dfs(node.left, targetSum, psum, path)
            dfs(node.right, targetSum, psum, path)
            path[psum] -= 1
            psum -= node.val
            
        
        dfs(root, targetSum, 0, path)
        return ans
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = collections.Counter()
        count[0] = 1
        ans = 0
        def dfs(node, p_sum):
            if node is None: return 0
            
            p_sum += node.val
            nonlocal ans
            if p_sum == targetSum: ans += count[0]
            else: ans += count[p_sum - targetSum]
            count[p_sum] += 1
            dfs(node.left, p_sum)
            dfs(node.right, p_sum)
            count[p_sum] -= 1

        dfs(root, 0)        
        return ans


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        count = collections.Counter()

        def dfs(node, s, path):
            nonlocal ans
            if node is None: return 0
            s += node.val
            
            if s == targetSum: 
                ans += count[0] + 1
            else: 
                ans += count[s - targetSum]
            
            count[s] += 1
            dfs(node.left, s, path)
            dfs(node.right, s, path)
            count[s] -= 1
            s -= node.val


        dfs(root, 0, [])
        return ans