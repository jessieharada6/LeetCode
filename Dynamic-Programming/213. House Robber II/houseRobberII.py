class Solution:
    def rob(self, nums: List[int]) -> int:
        def robOption(nums, start, end):
            rob1 = 0
            rob2 = 0
            
            for i in range(start, end):
                cur_max = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = cur_max
            
            return rob2
        
        return max(
            # -1 will not work as len(nums) - 1, only when getting an element nums[-1] works, which gets the last element in the array
            nums[0], robOption(nums, 0, len(nums) - 1), robOption(nums, 1, len(nums))
        )
