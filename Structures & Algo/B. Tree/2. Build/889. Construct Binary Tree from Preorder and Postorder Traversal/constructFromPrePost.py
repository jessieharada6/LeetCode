# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return
        
        root = TreeNode(preorder[0])    # postorder.pop()
        if len(preorder) == 1:          # leaf nodes or only one node
            return root
        
        l = preorder[1]                 # all left nodes
        size = postorder.index(l) + 1
        
        root.left = self.constructFromPrePost(preorder[1: size + 1], postorder[:size])
        root.right = self.constructFromPrePost(preorder[size + 1:], postorder[size:])
        
        return root

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, postorder, lpre, rpre, lpost, rpost):
            if lpre > rpre:
                return
            
            root = TreeNode(preorder[lpre])
            if lpre == rpre:
                return root
            
            l = preorder[lpre + 1]
            index = 0
            for i in range(lpost, rpost + 1):
                if postorder[i] == l:
                    index = i
                    break
                
            
            root.left = build(preorder, postorder, lpre + 1, lpre + 1 + index - lpost, lpost, index)
            root.right = build(preorder, postorder, lpre + 1 + index - lpost + 1, rpre, index + 1, rpost - 1)
            
            return root
        
        return build(preorder, postorder, 0, len(preorder) - 1, 0, len(postorder) - 1)
        