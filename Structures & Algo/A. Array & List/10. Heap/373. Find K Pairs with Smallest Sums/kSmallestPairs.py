class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for num in nums1:
            heappush(heap, (num + nums2[0], num, nums2[0], 0))
        
        ans = []
        
        while heap and k > 0:
            _, n1, n2, j = heappop(heap)
            ans.append([n1, n2])
            k -= 1
            
            nxt = j + 1
            if nxt < len(nums2):
                heappush(heap, (n1 + nums2[nxt], n1, nums2[nxt], nxt))
        
        return ans

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
        