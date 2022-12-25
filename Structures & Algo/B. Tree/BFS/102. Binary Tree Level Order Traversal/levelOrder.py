# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None: return ans
        cur = [root]

        while cur:
            ans.append([node.val for node in cur])
            nxt = []
            for node in cur:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt

        return ans

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None: return ans
        cur = collections.deque([root])

        while cur:
            ans.append([node.val for node in cur])

            for _ in range(len(cur)):
                node = cur.popleft()
                if node.left: cur.append(node.left)
                if node.right: cur.append(node.right)

        return ans