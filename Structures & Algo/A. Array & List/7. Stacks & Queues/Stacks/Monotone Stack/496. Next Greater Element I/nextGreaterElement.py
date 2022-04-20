class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        res = {}
        
        for n in nums2[::-1]: # keep a dictionary for nums2
            while s and s[-1] <= n:
                s.pop()
            
            res[n] = s[-1] if s else -1
            s.append(n)
        
        return [res[n] for n in nums1] # use key to get the nums1 next greater element