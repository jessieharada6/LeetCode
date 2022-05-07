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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = defaultdict(int)
        dup = []
        
        def find(root):
            if root is None:    
                return "#"                              # at leaf node, add # to key
            
            l = find(root.left)
            r = find(root.right)
            
            k = str(root.val) + "." + l + "." + r + "." # essential to add special char to distinguish value 
                                                        # e.g. 1, 11 or 11, 1
            seen[k] += 1
            
            if seen[k] == 2:
                dup.append(root)
            
            return k                                    # return key to save to seen
        
        find(root)
        return dup