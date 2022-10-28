class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        diff = inf
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 假设题目是找到一个target
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    # 题目说 必然有一个解
                    return s
                
                # 用距离(abs(s - target))判断是否找到一个更合适的ans
                if abs(s - target) < diff:
                    diff = min(diff, abs(s - target))
                    ans = s
        
        return ans
        