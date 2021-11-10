class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        # sort the array ascendingly
        nums = sorted(nums)
        output = []

        
        for i in range(len(nums)):
            # if the most left num is > 0, break the loop
            if nums[i] > 0:
                break
            # to avoid duplication, if the num is the same next to each other
            # don't add to the current
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                # get the sum
                # if 0, form triplets
                current = nums[i] + nums[l] + nums[r]
                if current == 0:
                    output.append([nums[i],nums[l], nums[r]])
                    # skip repetition
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # move pointers
                    l += 1
                    r -= 1
                elif current < 0:
                    l += 1
                elif current > 0:
                    r -= 1
                
        return output
                    
            