# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"] 
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, path):
            if node is None: return
            if node.left is node.right:  # leaf node
                path += str(node.val)
                ans.append(path)
                return
            path += str(node.val) + "->"
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        return ans

# Output: ["5->2->1","3->1"]
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, path):
            if not node: return
            if node.left is node.right:
                nonlocal ans
                path += str(node.val)
                p = path[::-1]
                ans.append("->".join(p))
                path.pop()
                return
            
            path.append(str(node.val))
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
        return ans