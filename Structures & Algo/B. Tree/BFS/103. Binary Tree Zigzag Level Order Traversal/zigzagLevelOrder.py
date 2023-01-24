# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        cur = [root]
        zig = False
        ans = []
        path = []

        while cur:
            # print(cur)
            path = [node.val for node in cur]
            ans.append(path if not zig else path[::-1])
            nxt = []
            for node in cur:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            zig = not zig
        
        return ans
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None: return ans
        cur = collections.deque([root])
        flag = False

        while cur:
            vals = [node.val for node in cur] 
            ans.append(vals if not flag else vals[::-1]) 
            flag = not flag
            for _ in range(len(cur)):
                node = cur.popleft()
                if node.left: cur.append(node.left)
                if node.right: cur.append(node.right)
                  
        return ans
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        if root is None:
            return ans
        
        level = [root]
        z = False                       # true if zigzag
        while level:
            nextLevel = []
            cur = []
            for node in level:
                cur.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            z = not z
            level = nextLevel
            
            ans.append(cur if z else list(reversed(cur)))
        
        return ans
            