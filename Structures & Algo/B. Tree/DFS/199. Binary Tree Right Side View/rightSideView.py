# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        def dfs(node, depth):
            if node is None: return

            if len(rightSide) == depth:
                rightSide.append(node.val)
            
            r = dfs(node.right, depth + 1)
            l = dfs(node.left, depth + 1)
            
        
        dfs(root, 0)
        return rightSide

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        curDepth = -1
        def dfs(node, depth):
            if node is None: return
            
            nonlocal curDepth
            if curDepth < depth:
                rightSide.append(node.val)
                curDepth = depth
            # print(node.val, depth, curDepth)
            r = dfs(node.right, depth + 1)
            l = dfs(node.left, depth + 1)
            
        
        dfs(root, 0)
        return rightSide

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


