# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        print(root)
        print([root])
           
        depth = 0
        levels = [root] if root else []
        
        while levels:
            depth += 1
            queue = []
            
            for level in levels:
                if level.left:
                    queue.append(level.left)
                if level.right:
                    queue.append(level.right)
                
            levels = queue
        
        return depth


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        # last leaf's left and right is max(0, 0) + 1 to get back to the leaf
        # max(left, right) + 1(current node)
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
     
            
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth = 0
        queue = collections.deque([root])
        
        while queue:
            depth += 1
            
            # len(queue) is the current length each time before entering the for loop
            for i in range(len(queue)):
                # popleft is O(1), faster than pop
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        
        return depth
                 