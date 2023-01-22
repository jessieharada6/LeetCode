# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        
        right_side = []
        cur = [root]
        while cur:
            length = len(cur)
            prev = []
            for idx, node in enumerate(cur):
                if node.left:
                    prev.append(node.left)
                if node.right:
                    prev.append(node.right)
                if idx + 1 == length:
                    right_side.append(node.val)
            
            cur = prev
        
        return right_side
        