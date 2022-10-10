class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ors = []
        
        for i in range(len(nums) - 1, -1, -1):
            ors.append([0, i])
            k = 0
            for o in ors:
                o[0] |= nums[i]
                if ors[k][0] == o[0]:
                    ors[k][1] = o[1]
                else:
                    k += 1
                    ors[k] = o
            
            del ors[k + 1:]
            ans[i] = ors[0][1] - i + 1

        return ans


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i, x in enumerate(nums):
            for j in range(i - 1, -1, -1):
                if nums[j] | x == nums[j]:
                    break
                nums[j] |= x
                
                ans[j] = i - j + 1
        
        return ans