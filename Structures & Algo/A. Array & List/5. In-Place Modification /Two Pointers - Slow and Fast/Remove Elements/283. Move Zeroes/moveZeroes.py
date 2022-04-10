class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # move 0 to the end == remove 0
        
        # 1. remove elements
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        # 2. assign the rest of elements to 0
        for i in range(slow, len(nums)):
            nums[i] = 0
        



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == 0:
                if nums[fast] != 0:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                    slow += 1
            else:
                slow += 1
            fast += 1
        
        print(nums)