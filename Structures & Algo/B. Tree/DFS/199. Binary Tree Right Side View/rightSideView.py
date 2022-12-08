# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = 0
        def dfs(node, depth):
            nonlocal cur
            if node is None: return

            if depth - cur == 1:
                ans.append(node.val)
                cur = depth
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 1)
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