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