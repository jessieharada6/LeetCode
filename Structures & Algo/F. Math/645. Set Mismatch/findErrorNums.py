class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = -1
        for i in range(n):
            index = abs(nums[i]) - 1 # no list out of boundary
            if nums[index] < 0:
                dup = abs(nums[i]) # found dup
            else:
                nums[index] *= -1

        missing = -1
        for i in range(n):
            if nums[i] > 0: # missing index will not be negative
                missing = i + 1
        
        return [dup, missing]
        


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict = defaultdict(int)
        for i in range(1, len(nums) + 1):
            dict[i] = 0
        
        # print(dict)
        
        for n in nums:
            dict[n] += 1
        
        # print(dict)
        
        ans = [0] * 2
        
        for k, v in dict.items():
            if dict[k] == 2:
                ans[0] = k
            if dict[k] == 0:
                ans[1] = k
        
        return ans
        
        