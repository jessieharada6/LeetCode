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
       