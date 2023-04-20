# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # 空节点被cam覆盖: inf - 当非空节点得到这个值可以min变成1-如果这棵树只有一个node
            # 空节点被小孩/长辈覆盖: 0 - 当前空节点需要0个cam
            if node is None: return inf, 0, 0 

            l = dfs(node.left)
            r = dfs(node.right)

            # 当前节点被cam覆盖
            #   随意搭配：小孩和长辈可有可无 + 1(当前节点的cam)
            w_cam = min(l[0],l[1],l[2]) + min(r[0],r[1],r[2]) + 1 
            # 当前节点被小孩覆盖
            #    左右小孩都有cam
            #    左小孩有cam 有小孩没有cam
            #    左小孩没有cam 有小孩有cam
            no_cam_but_children = min(l[0] + r[0], l[0] + r[1], l[1] + r[0])
            # 当前节点被长辈覆盖：但是长辈我们不知道情况，换个角度看小孩
            #    左右小孩都有cam 
            #    左小孩有cam 有小孩没有cam
            #    左小孩没有cam 有小孩有cam
            #    左右小孩都没有cam - 反正长辈有cam
            no_cam_but_parent = min(l[0],l[1]) + min(r[0],r[1])

            return w_cam, no_cam_but_children, no_cam_but_parent
        
        res = dfs(root)
        return min(res[0], res[1]) # 此时是root不会有长辈