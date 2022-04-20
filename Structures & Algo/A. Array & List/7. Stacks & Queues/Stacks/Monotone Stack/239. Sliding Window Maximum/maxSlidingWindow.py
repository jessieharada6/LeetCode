


# use collections.deque or stack as below
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = []
        ans = []
        l = r = 0
        
        while r < len(nums):
            while s and nums[s[-1]] < nums[r]:
                s.pop()
            s.append(r)
            
            if r >= k - 1:
                ans.append(nums[s[0]])
                l += 1
            
            if l > s[0]:
                s.pop(0)
                
            r += 1
        
        return ans