class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n % 2 == 1:
            return nums[int((n - 1) / 2)]
        else:
            num1 = nums[int(n / 2)]
            num2 = nums[int(n / 2) - 1]
            return (num1 + num2) / 2
