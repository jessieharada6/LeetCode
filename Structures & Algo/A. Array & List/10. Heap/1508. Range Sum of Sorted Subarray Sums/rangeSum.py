class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans, mod = 0, 10 ** 9 + 7
        
        heap = []
        for j in range(n):
            heappush(heap, (nums[j], j))
        
        for i in range(right):
            s, j = heappop(heap)
            if j + 1 < n:
                heappush(heap, (s + nums[j + 1], j + 1))
            
            if i >= left - 1:
                ans = (ans + s) % mod
        
        return ans  


        class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def rank(val):
            i, cnt = 0, 0
            for j in range(1, len(nums)):
                dist = nums[j] - nums[i]
                if dist > k:
                    i += 1
                cnt += j - i
                print(cnt, dist, i, j)
            return cnt
        
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = l + (r - l) // 2
            print(m)
            if rank(m) < k:
                l = m + 1
            else:
                r = m
        
        return l
                