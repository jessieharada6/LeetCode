# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        if root is None:
            return ans
        
        level = [root]
        z = False                       # true if zigzag
        while level:
            nextLevel = []
            cur = []
            for node in level:
                cur.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            z = not z
            level = nextLevel
            
            ans.append(cur if z else list(reversed(cur)))
        
        return ans
            