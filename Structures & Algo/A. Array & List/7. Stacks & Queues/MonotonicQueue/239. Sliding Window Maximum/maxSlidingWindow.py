class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        s = collections.deque()
        l = r = 0
        
        while r < len(nums):
            while s and nums[s[-1]] < nums[r]:
                s.pop() 
            s.append(r)
            
            r += 1
            
            if r - l >= k:
                ans.append(nums[s[0]])
                l += 1
            
            if l > s[0]:
                s.popleft()
            
            # print(l, r, s, ans)
        
        return ans