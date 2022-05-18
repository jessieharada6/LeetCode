# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(lo, hi):
            trees = []
            if lo > hi:
                trees.append(None)
            
            for r in range(lo, hi + 1):
                left = build(lo, r - 1)
                right = build(r + 1, hi)
                
                for _l in left:
                    for _r in right:
                        root = TreeNode(r)
                        root.left = _l
                        root.right = _r
                        trees.append(root)
            return trees                                # update built trees
        
        return build(1, n)
        
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(l, r):
            trees = []
            if l > r:
                trees.append(None)                  # when 1 > 0, 1 as a root has no children
                                                    # when l == r, it is a leaf node   
            for n in range(l, r + 1):
                                                    # left and right are unique as we only traverse each range once
                left = build(l, n - 1)  
                right = build(n + 1, r)
                
                for _l in left:                     # left and right are presented as arrays
                    for _r in right:
                        root = TreeNode(n)          # build root based on different combo of left and right
                        root.left = _l
                        root.right = _r
                        trees.append(root)          # append the unique tree
            return trees
        
        return build(1, n)

