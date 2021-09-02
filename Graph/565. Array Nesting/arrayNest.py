class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_size = 0
        
        for current_index in range(len(nums)):
            size = 0
            
            while nums[current_index] >= 0:
                size += 1
                prev_index = current_index
                current_index = nums[current_index]
                nums[prev_index] = -1 
                
            max_size = max(size, max_size)
            
        return max_size