class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        heapq.heapify(queue)
        
        for n in nums:
            heapq.heappush(queue, n) # push the smallest item as first item
            
            if len(queue) > k:
                heapq.heappop(queue) # pop the smallest item as first item
           
        
        return heapq.heappop(queue)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        
        while True:
            pos = self.position(nums, left, right)
            # print(pos)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 > k:
                right = pos - 1
            elif pos + 1 < k:
                left = pos + 1
                
        
    def position(self, nums, left, right):
        pivot = nums[left]
        l = left + 1
        r = right
        # print("l:", l, " r:", r)
        
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                self.swap(nums, l, r)
                l += 1
                r -= 1
                
            if nums[l] >= pivot: l += 1
            if nums[r] <= pivot: r -= 1
            
        self.swap(nums, left, r)
        # print(left, right, l, r, nums)
        return r
    
    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]