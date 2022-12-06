# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(nodeP, nodeQ) -> bool:
            if not nodeP and not nodeQ: return True
            if not nodeP and nodeQ: return False
            if nodeP and not nodeQ: return False
            if nodeP.val != nodeQ.val: return False
            return dfs(nodeP.left, nodeQ.left) and dfs(nodeP.right, nodeQ.right)
        
        return dfs(p, q)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(root):
            if root is None:
                return "#"
            
            l = traverse(root.left)
            r = traverse(root.right)
            
            return str(root.val) + "," + l + "," + r
        
        return traverse(p) == traverse(q)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # same nodes: check values and positions
        if p and q:
            #print(p.val, q.val)
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        #print(p, q)
        
        # if same tree, now p and q should be both None
        # dif nodes/same nodes diff positions: one of the trees wil have elements left 
        return p == None and q == None # p is q