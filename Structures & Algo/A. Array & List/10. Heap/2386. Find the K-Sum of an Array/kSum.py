class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        for i, n in enumerate(nums):
            if n >= 0:
                max_sum += n
            else:
                nums[i] = -n
        
        nums.sort()
        
        
        heap = [(-max_sum, 0)]
        for _ in range(k - 1):
            s, i = heappop(heap)
            
            if i < len(nums):
                heappush(heap, (s + nums[i], i + 1))
                if i:
                    heapq.heappush(heap, (s + nums[i] - nums[i - 1], i + 1))
        return -heap[0][0]