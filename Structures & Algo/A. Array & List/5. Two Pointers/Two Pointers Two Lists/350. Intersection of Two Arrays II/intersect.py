class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        ans = []
        i = j = 0
        # 每一次进入循环只有一种情况可以被判断  
        # 用if else 而非平行if（且会超出index）
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
            
        return ans
        
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 统计其中一个数组的次数
        # 看长数组是否有匹配的数字
        
        m, n = len(nums1), len(nums2)
        cnt = Counter()
        ans = []
        for x in nums1:
            cnt[x] += 1

        for x in nums2:
            if cnt[x] != 0:
                ans.append(x)
                cnt[x] -= 1
        
        
        return ans
       