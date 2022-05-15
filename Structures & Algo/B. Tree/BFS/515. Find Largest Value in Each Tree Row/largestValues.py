# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        
        level = [root]
        
        while level:
            next_level = []
            cur = []
            for node in level:
                cur.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
            ans.append(max(cur))
        
        return ans


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        
        level = [root]
        
        while level:
            size = len(level)
            cur = []
            for i in range(size):
                node = level.pop(0)
                cur.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ans.append(max(cur))
        
        return ans