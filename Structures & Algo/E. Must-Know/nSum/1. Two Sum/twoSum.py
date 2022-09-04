class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict()
        for i, n in enumerate(nums):
            map[n] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in map and map[diff] != i:
                return [i, map[diff]]