# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def traverse(root):
            nonlocal max_sum
            if root is None:
                return 1, inf, -inf, 0      
            
            is_l, min_l, max_l, sum_l = traverse(root.left)
            is_r, min_r, max_r, sum_r = traverse(root.right)
            
            if is_l and is_r and max_l < root.val < min_r:
                cur = sum_l + sum_r + root.val
                max_sum = max(cur, max_sum)
                min_l = min(min_l, root.val)
                max_r = max(max_r, root.val)
                return 1, min_l, max_r, cur
            else:
                return 0, 0, 0, 0
                
        traverse(root)
        return max_sum
        
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
                # print(is_l, min_l, max_l, sum_l, max_sum, root.val)
                # print(is_r, min_r, max_r, sum_r, max_sum, root.val)
                return 1, minl, maxr, cur
            else:
                # print(min_l, max_l, max_sum, root.val)
                # print(min_r, max_r, max_sum, root.val)
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