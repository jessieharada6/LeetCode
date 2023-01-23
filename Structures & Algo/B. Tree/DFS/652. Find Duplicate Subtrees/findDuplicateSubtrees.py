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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = collections.Counter()
        ans = []
        def dfs(node):
            path = ""                   # path每一次都是空的 已经走过的path返回到了l和r
            if node is None: return "#"

            l = dfs(node.left)
            r = dfs(node.right)

            # 直接加node是不行的 因为对象是独立存在的
            path += str(node.val) + "." + l + "." + r + "."

            count[path] += 1
            if count[path] == 2:
                ans.append(node)
            return path
        
        dfs(root)
        return ans

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        paths = []
        seen = collections.defaultdict(int)
        def dfs(node, path):
            if node is None: return "o"

            l = dfs(node.left, path)
            r = dfs(node.right, path)
            path = str(node.val) + "." + l + "." + r + "."
            seen[path] += 1
            if seen[path] == 2:
                paths.append(node)

            return path
        dfs(root, "")
        return paths

        
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