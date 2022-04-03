class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l = r = 0
        ans = []
        
        while r < len(nums):
            # when the min is smaller than the current num
            # constantly pop in the same window, leave the max
            while q and nums[q[-1]] < nums[r]: 
                q.pop()
            q.append(r) # append index
            
            if l > q[0]: ## not while as we care about the max, and the while loop above will take care of the max
                q.popleft() 
                
            if r >= k - 1:
                ans.append(nums[q[0]])
                l += 1 # start a new window
            r += 1
        
        return ans

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
            
            #  new starting point of l -> q[0] out of range 
            if l > q[0]: 
                q.popleft()
            
            r += 1
        
        return ans