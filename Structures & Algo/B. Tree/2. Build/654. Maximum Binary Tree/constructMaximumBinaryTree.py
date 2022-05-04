# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:  # due to root_index, the range of construction changes 
            return
        
        root_val = max(nums)
        root_index = nums.index(root_val)

        root = TreeNode(root_val)
        root.left = self.constructMaximumBinaryTree(nums[0: root_index])                #[0:root_index-1]
        root.right = self.constructMaximumBinaryTree(nums[root_index + 1: len(nums)])   #[root_index:len(nums) - 1]
        
        return root


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums, l, r):
            if l == r:     # l index and r index are equal when it is an empty array
                return None
            
            root_val = -1
            root_index = -1
            for i in range(l, r):
                if root_val < nums[i]:
                    root_val = nums[i]
                    root_index = i
            
            root = TreeNode(root_val)
            root.left = build(nums, l, root_index)
            root.right = build(nums, root_index + 1, r)
            
            return root
        
        return build(nums, 0, len(nums))

# 解释：递归调用如下所示：
# - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
#     - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
#         - 空数组，无子节点。
#         - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
#             - 空数组，无子节点。
#             - 只有一个元素，所以子节点是一个值为 1 的节点。
#     - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
#         - 只有一个元素，所以子节点是一个值为 0 的节点。
#         - 空数组，无子节点。
# source: https://leetcode-cn.com/problems/maximum-binary-tree/solution/-by-gracious-vvilson1bb-sa5e/