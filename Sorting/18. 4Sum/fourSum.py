class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        nums = sorted(nums)
        output = []
        
        for i in range(len(nums)):
            # no longer 0 as target
            #if nums[i] > target:
                #break
                        
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1
                
                # same way as i 
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                while l < r:
                    current = nums[i] + nums[j] + nums[l] + nums[r]
                    #print(i, j, l, r, current)
                    if current == target:
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l+=1
                        while l < r and nums[r] == nums[r - 1]:
                            r-=1
                        l += 1
                        r -= 1
                    elif current < target:
                        l += 1
                    elif current > target:
                        r -= 1

        return output