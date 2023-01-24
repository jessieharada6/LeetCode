# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0

        while q:
            ans = 0
            for _ in range(len(q)):
                node = q.popleft()
                ans += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return ans
        
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        cur = collections.deque([root])

        while cur:
            ans = 0
            for node in cur:
                ans += node.val 
            for _ in range(len(cur)):
                node = cur.popleft()
                if node.left:   
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)

        return ans