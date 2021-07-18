# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            return TreeNode(val, root)
        
        queue = []
        queue.append(root)
        
        while len(queue):
            size = len(queue)
            depth -= 1
            for _ in range(size):
                current = queue.pop(0)
                if depth == 1:
                    current.left = TreeNode(val, current.left)
                    current.right = TreeNode(val, None, current.right)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
        return root
                