class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        ans = []
        q = collections.deque()
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # num in q is smaller than the current num
                q.pop() # pop from the right side one by one
            q.append(r) # use index to know where we are at
            
            if r >= k - 1: # start to get the values from k - 1 position
                ans.append(nums[q[0]])
                l += 1 # slide 
            
            if l > q[0]: #  new starting point of l -> q[0] out of range 
                q.popleft()
            
            r += 1
        
        return ans