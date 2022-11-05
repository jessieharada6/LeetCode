#当目标是<时
#>=可以归为一类 即 对立情况

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            if nums[i] + nums[i + 1] + nums[i + 2] > target:
                break
            # 不可以这样优化 因为j可以游走在之前的值从而使得s变小
            # if nums[i] + nums[-1] + nums[-2] == target:
            #     continue
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    ans += k - j
                    j += 1
                else:
                    k -= 1

        return ans