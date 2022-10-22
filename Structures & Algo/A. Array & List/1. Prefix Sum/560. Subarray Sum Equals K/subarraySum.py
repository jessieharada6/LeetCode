class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 当前点总和 - 记录过的前缀和 = k
        # k：当前点(right)到之前的某点(left)的和 l <= r
        # 当前点总和 - k = 记录过的前缀和
        
        # 记录过的前缀和 初始为 0 因为第一个数字的前缀和是 0
        
        ans = 0
        psum = 0
        cnt = Counter()
        cnt[0] = 1
        
        for x in nums:
            psum += x
            if psum - k in cnt:
                ans += cnt[psum - k]
            cnt[psum] += 1
        
        return ans