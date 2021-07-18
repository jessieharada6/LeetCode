class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        # for index, val in enumerate(list)
        for i, num in enumerate(nums):
            dict[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            # diff in dict needs to be checked first to avoid exception
            if diff in dict and dict[diff] != i:
                return [dict[diff], i]