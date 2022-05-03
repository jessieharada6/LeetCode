# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 
        
        root_val = max(nums)
        root_index = nums.index(root_val)
        
        root = TreeNode(root_val)
        root.left = self.constructMaximumBinaryTree(nums[0:root_index])                 #[0:root_index-1]
        root.right = self.constructMaximumBinaryTree(nums[root_index + 1:len(nums)])    #[root_index:len(nums) - 1]
        
        return root
