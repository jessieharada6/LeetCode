# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(int)
        dup = []
        
        def dfs(root):
            if root is None:
                return "#"                                  # note
            
            l = dfs(root.left)
            r = dfs(root.right)
                
            subtree = str(root.val)  + "_" + l + "_" + r   # note: to avoid [2,1,11,11,null,1] forming the same sequence 11,1 and 1,11, use "_" to separate
            
            if count[subtree] == 1:
                dup.append(root)
                
            count[subtree] += 1
            
            return subtree                                  # note
        
        dfs(root)
        # print(count)
        return dup