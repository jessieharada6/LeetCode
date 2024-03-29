# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return root
        if p.val == root.val or q.val == root.val: return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r: return root
        return l if l else r

class Solution:
    # 函数定义：是否找到了lca
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return root
        
        # q如果在p下面 返回
        # q如果不在p下面 返回当前找到的p
        if root.val == p.val or root.val == q.val:
            return root  # 归上去
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # l, r-找到的val 没找到return None
        if l and r: return root
        return l if l else r
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return root
        if p.val == root.val or q.val == root.val: return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        print(root.val, l, r)
        if l and r: 
            print("l, r")
            return root
        if l: 
            print("l")
            return l
        if r:
            print("r")
            return r