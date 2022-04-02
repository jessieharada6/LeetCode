class Solution:
    def preimageSizeFZF(self, k: int) -> int:           
        # 172. https://leetcode.com/problems/factorial-trailing-zeroes/submissions/
        def trailingZeroes(n) -> int: 
            ans = 0
            while n != 0:
                cur = n // 5 # floor division
                ans += cur

                n = cur
            return ans
        
        def leftBound(k):
            l = 0
            r = int(5e9)
            while l < r:
                m = l + (r - l) // 2
                if trailingZeroes(m) >= k:
                    r = m
                else:
                    l = m + 1
            return l
         
        def rightBound(k):
            l = 0
            r = int(5e9)
            while l < r:
                m = l + (r - l) // 2
                if trailingZeroes(m) > k:
                    r = m
                else:
                    l = m + 1
            return r
        
        
        l = leftBound(k)
        r = rightBound(k)
        # print(l, r)
        return r - l