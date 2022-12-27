# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        root_idx = len(nums) // 2
        root = TreeNode(nums[root_idx])
        # if len(nums) == 1: return root
        root.left = self.sortedArrayToBST(nums[:root_idx])
        root.right = self.sortedArrayToBST(nums[root_idx + 1:])
        return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        root_idx = len(nums) // 2
        return TreeNode(nums[root_idx], self.sortedArrayToBST(nums[:root_idx]), self.sortedArrayToBST(nums[root_idx + 1:]))