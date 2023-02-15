class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # @cache
        # def dfs(i):
        #     if i < 0: return 0
        #     return max(nums[i] + dfs(i - 2), dfs(i - 1))
        # return dfs(n - 1)

        # f = [0] * (n + 2)
        # for i in range(2, len(f)):
        #     f[i] = max(nums[i - 2] + f[i - 2], f[i - 1])
        # return f[-1]

        a, b = 0, 0
        for x in nums:
            a, b = b, max(x + a, b)
        return b

###
# 1.
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {0: nums[0]}
        def dfs(i):
            if i < 0: return 0
            # if i == 0: return nums[i]
            if i in cache:
                return cache[i]

            ans = max(dfs(i - 1), nums[i] + dfs(i - 2))
            cache[i] = ans
            return ans

        dfs(len(nums) - 1)
        return cache[len(nums) - 1]

# 2.
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i < 0: return 0

            if i in cache:
                return cache[i]

            ans = max(dfs(i - 1), nums[i] + dfs(i - 2))
            cache[i] = ans
            return ans

        return dfs(len(nums) - 1)

# 3.
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 2)
        for i in range(2, n + 2):
            num = max(f[i - 1], nums[i - 2] + f[i - 2])
            f[i] = num
        
        print(f)
        return f[-1]

# 4.
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = 0, 0
        for i in range(2, n + 2):
            b, a = max(a + nums[i - 2], b), b
        return b
        
# 5.
class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for x in nums:
            b, a = max(a + x, b), b
        return b