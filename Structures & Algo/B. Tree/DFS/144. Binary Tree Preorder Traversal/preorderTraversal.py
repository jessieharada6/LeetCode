# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use children trees to get the entire trees
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        
        res.append(root.val)
        res += self.preorderTraversal(root.left)  # same as .extend
        res += self.preorderTraversal(root.right)
        
        return res

# dfs traversal
class Solution:
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return self.res
        
        self.res.append(root.val)
        self.preorderTraversal(root.left)  
        self.preorderTraversal(root.right)
        
        return self.res