class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        final_max = nums[0]
        
        for i in range(1, len(nums)):
            # when nums[i] < 0
            # the future cur_max is cur_min
            # vice versa
            if nums[i] < 0:
                temp = cur_max
                cur_max = cur_min
                cur_min = temp

            cur_max = max(cur_max * nums[i], nums[i])
            cur_min = min(cur_min * nums[i], nums[i])

            final_max = max(cur_max, final_max)
        
        return final_max