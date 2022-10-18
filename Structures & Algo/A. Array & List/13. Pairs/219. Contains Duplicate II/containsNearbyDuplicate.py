class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        
        for r, num in enumerate(nums):
            if num in d and r - d[num] <= k:
                return True
            d[num] = r
        
        return False