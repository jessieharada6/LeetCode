# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left = 0
        cur = deque([root])
        while cur:
            for _ in range(len(cur)):
                node = cur.popleft()
                if node.right: cur.append(node.right)
                if node.left: cur.append(node.left)
                left = node.val
        
        return left
        
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        cur = collections.deque([root])
        while cur:
            for i in range(len(cur)):
                node = cur.popleft()
                if i == 0:
                    ans = node.val 
                if node.left: cur.append(node.left)
                if node.right: cur.append(node.right)
        return ans

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        cur = collections.deque([root])
        while cur:
            ans = cur[0].val
            for i in range(len(cur)):
                node = cur.popleft()
                if node.left: cur.append(node.left)
                if node.right: cur.append(node.right)
        return ans

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        cur = collections.deque([root])
        while cur:
            for i in range(len(cur)):
                node = cur.popleft()
                if node.right: cur.append(node.right)
                if node.left: cur.append(node.left)
                
        return node.val