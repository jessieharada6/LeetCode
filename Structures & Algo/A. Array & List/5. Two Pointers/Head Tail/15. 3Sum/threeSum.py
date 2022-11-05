class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i < j < k
        # i: [0 : len(nums) - 2)
        # j: i + 1
        # k: [j + 1 : len(nums) - 1]
        
        ans = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            # 在进入j++ k--之前 先进行比较 判断是否值得进入循环
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
                
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return ans
        

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i < j < k
        # 0 <= i < len(nums) - 2
        # i < j < k: j = i + 1
        # len(nums) - 1 >= k > j: k = len(nums) - 1
        
        ans = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # 判断i
            if i and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    # 判断j和k
                    j += 1  # 保证j的存在
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1  # 保证k的存在
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        
        return ans
                    
                
                