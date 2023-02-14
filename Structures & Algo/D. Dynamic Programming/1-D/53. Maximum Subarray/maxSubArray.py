# 以i为结尾的非空最大子数组和
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
    
        @cache
        def dfs(i) -> int:
            if i < 0: return 0
            # if i == 0: return nums[0]
            # nums[i] 必选 以满足以i为结尾的最大子数组和 不选会断-就不是子数组了
            return max(nums[i] + dfs(i - 1), nums[i])
        
        ans = -inf
        for i in range(n):
            res = dfs(i)
            ans = max(res, ans)
        return ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i) -> int:
            if i < 0: return 0
            return max(nums[i] + dfs(i - 1), nums[i])

        return max(dfs(i) for i in range(n))

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        f = [0] * n
        f[0] = nums[0]
        for i in range(1, n):
            f[i] = max(nums[i] + f[i - 1], nums[i])
        return max(f)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans, b = -inf, -inf
        for x in nums:
            b = max(x + b, x)
            ans = max(ans, b)

        return ans

###
# 1. 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = {}
        def dfs(end):
            if end == 0: return nums[0]
            if end in cache:
                return cache[end]

            ans = max(nums[end] + dfs(end - 1), nums[end])
            cache[end] = ans 
            return ans
        
        ans = -math.inf
        for i in range(len(nums)):
            # print(i, dfs(i))
            # 把每一个i当作结尾 因为最大值可能不是在最后一个i (len(nums) - 1)
            # 如果没有for loop,会返回以最后一个i (len(nums) - 1)
            ans = max(ans, dfs(i))
        return ans

# 2. 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def dfs(end):
            if end == 0: return nums[0]
            return max(nums[end] + dfs(end - 1), nums[end])
        
        ans = -math.inf
        for i in range(len(nums)):
            # print(i, dfs(i))
            ans = max(ans, dfs(i))
        return ans

# 3. 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def dfs(end):
            if end == 0: return nums[0]
            return max(nums[end] + dfs(end - 1), nums[end])
        
        return max(dfs(i) for i in range(len(nums)))

# 4.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        for i in range(1, n):
            f[i] = max(nums[i] + f[i - 1], nums[i])

        return max(f)

# 5.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans, a, b = nums[0], nums[0], nums[0]

        for i in range(1, n):
            a, b = b, max(nums[i] + b, nums[i])
            ans = max(ans, b)
            
        return ans

# 6.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans, _, b = nums[0], nums[0], nums[0]

        for i in range(1, n):
            _, b = b, max(nums[i] + b, nums[i])
            ans = max(ans, b)
            
        return ans

# 7.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans, b = nums[0], nums[0]

        for i in range(1, n):
            b = max(nums[i] + b, nums[i])
            ans = max(ans, b)
            
        return ans

# 8.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, b = -math.inf, -math.inf

        for x in nums:
            b = max(x + b, x)
            ans = max(ans, b)
            
        return ans

###
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
    
        # @cache
        # def dfs(i) -> int:
        #     if i < 0: return 0
        #     # if i == 0: return nums[0]

        #     return max(nums[i] + dfs(i - 1), nums[i])
        
        # # ans = -inf
        # # for i in range(n):
        # #     res = dfs(i)
        # #     ans = max(res, ans)
        # return max(dfs(i) for i in range(n))

        # f = [0] * n
        # f[0] = nums[0]
        # for i in range(1, n):
        #     f[i] = max(nums[i] + f[i - 1], nums[i])
        # return max(f)

        a, b = 0, nums[0]
        ans = nums[0]
        for i in range(1, n):
            a, b = b, max(nums[i] + b, nums[i])
            ans = max(ans, b)
            print(a, b)
        return ans