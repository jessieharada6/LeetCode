class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        flag = (n := len(nums1)) > (m := len(nums2))
        if flag:
            n, m, nums1, nums2 = m, n, nums2, nums1
            
        heap = []
        for i in range(min(k, n)):
            heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        ans = []
        
        while heap and len(ans) < k:
            s, i, j = heappop(heap)
            if j + 1 < min(k, m):
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            ans.append([nums1[i], nums2[j]] if not flag else [nums2[j], nums1[i]])
            
        return ans
        