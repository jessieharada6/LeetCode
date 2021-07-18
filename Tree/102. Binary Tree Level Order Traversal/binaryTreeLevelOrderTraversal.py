# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        
        queue = []
        queue.append(root)
        
        while len(queue):
            size = len(queue)
            layer = []
            
            for _ in range(0, size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                layer.append(current.val)
            
            result.append(layer)
        
        return result