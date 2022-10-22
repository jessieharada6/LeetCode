class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # nums[j] - nums[i] = nums[k] - nums[j] = diff
        # i < k < j
        # 以每一个当前点为j i用来看-diff k用来看+diff
        # j的范围是[1,len(nums) - 1] 因为i和k需要在j的左右
        # dict来记录坐标 用来检查是否有满足条件的
        
        ans = 0
        
        d = defaultdict(list)
        for j, x in enumerate(nums):
            d[x].append(j)

            
        for j in range(1, len(nums) - 1):
            x = nums[j]
            
            if x - diff in nums and x + diff in nums:
                for i, k in zip(d[x - diff], d[x + diff]):
                    if i < j and j < k:
                        ans += 1
        
        return ans