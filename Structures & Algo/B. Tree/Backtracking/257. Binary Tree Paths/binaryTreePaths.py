# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def traverse(path, root):
            if not root:
                return
            if not root.left and not root.right:
                path.append(str(root.val))
                paths.append("->".join(path))
                path.pop()
                return
            
            path.append(str(root.val))
            traverse(path, root.left)
            traverse(path, root.right)
            path.pop()
        
        traverse([], root)
        return paths