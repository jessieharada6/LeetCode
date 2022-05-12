# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def t(root):
            nonlocal max_sum
            if root is None:
                return 1, inf, -inf, 0
            
            isl, minl, maxl, suml = t(root.left)
            isr, minr, maxr, sumr = t(root.right)
            
            if isl and isr and maxl < root.val < minr:
                minl = min(minl, root.val)
                maxr = max(maxr, root.val)
                cur = suml + sumr + root.val
                max_sum = max(cur, max_sum)
                return 1, minl, maxr, cur
            else:
                return 0,0,0,0
        
        t(root)
        return max_sum
        
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        sum_max = 0
        
        def traversal(root):
            if root is None:
                return (1, inf, -inf, 0)
            
            nonlocal sum_max
            
            # is_bst_l: 1 is valid, 0 is invalid
            # min: min val
            # max: max val
            # sum: current sum
            is_bst_l, min_val_l, max_val_l, sum_val_l = traversal(root.left)
            is_bst_r, min_val_r, max_val_r, sum_val_r = traversal(root.right)

            if is_bst_l and is_bst_r and max_val_l < root.val < min_val_r:
                cur_max = sum_val_l + sum_val_r + root.val      # current sum
                sum_max = max(cur_max, sum_max)
                min_val_l = min(min_val_l, root.val)            # current min 
                max_val_r = max(max_val_r, root.val)            # current max
                return 1, min_val_l, max_val_r, cur_max
                
            else:
                return 0, 0, 0, 0    

        traversal(root)   
        return sum_max