# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return 

        self.flatten(root.left)
        self.flatten(root.right)

        l = root.left
        r = root.right
        p = l
        while p and p.right: 
            p = p.right
        if p:
            p.right = r
            root.right = root.left
            root.left = None
            
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            return              # as the method returns None
        
                                # if using preorder, 
                                # need to check if every root.left is not null
                                # and go through the while loop below each time
        self.flatten(root.left)
        self.flatten(root.right)

                                # flattened left and right tree
        
        l = root.left
        r = root.right
                                
        root.left = None        
        root.right = l          # root connects to the left
        
        while root.right:
            root = root.right   # traverse 
                                # find the next position
        root.right = r          # connect the right side of the tree


class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            return

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root        # get sorted root


# 	root
#     / 
#   1 
#  / \ 
# 3  4  
# Let's see what is happening with this code.

# Node(4).right = None
# Node(4).left = None
# prev = Node(4)

# Node(3).right = Node(4) (prev)
# Node(3).left = None
# prev = Node(3)->Node(4)

# Node(1).right = prev = Node(3) -> Node(4)
# Node(1).left = None
# prev = Node(1)->Node(3)->Node(4) (Which is the answer)

# The answer use self.prev to recode the ordered tree of the right part of current node.
# Remove the left part of current node

# explaination from https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)