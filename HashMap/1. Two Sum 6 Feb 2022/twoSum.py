# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        # if nums[i] is the same, i will be the last index
        # [2,5,5,11]
        # {2: 0, 5: 2, 11: 3}
        numsDictionary = {nums[i] : i for i in range(len(nums))}
        
        
        # O(n)
        for i, num in enumerate(nums):
            diff = target - num
            
            # numsDictionary[diff] might not exist
            # e.g. 10 - 2 = 8 results in key error
            # if statement must check if diff is in the dictionary first
            # if not, short circuit and iterate to the next value
            if diff in numsDictionary and i != numsDictionary[diff]:
                return [i, numsDictionary[diff]]
        
            
            
# O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            current = nums[i]
            for j in range(i + 1, len(nums)):        
                if nums[i] + nums[j] == target:
                    return [i, j]
            