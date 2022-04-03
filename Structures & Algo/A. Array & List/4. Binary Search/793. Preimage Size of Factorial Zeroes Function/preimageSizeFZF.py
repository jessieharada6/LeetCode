class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def getTrailingZeros(n):
            ans = 0
            while n != 0:
                cur = n // 5
                ans += cur
                
                n = cur
            
            return ans
        
        def searchBound(target, left_biased):
            l = 0
            r = int(10e9)
            i = -1
            while l <= r:
                m = l + (r - l) // 2
                if getTrailingZeros(m) < k:
                    l = m + 1
                elif getTrailingZeros(m) > k:
                    r = m - 1
                elif getTrailingZeros(m) == k:
                    i = m
                    if left_biased:
                        r = m - 1
                    else: 
                        l = m + 1
            return i
        
        left = searchBound(k, True)
        right = searchBound(k, False)

        return right - left + 1 if left != -1 and right != -1 else 0
        

class Solution:
    def preimageSizeFZF(self, k: int) -> int:           
        # 172. https://leetcode.com/problems/factorial-trailing-zeroes/submissions/
        def trailingZeroes(n) -> int: 
            ans = 0
            while n != 0:
                cur = n // 5 # floor division
                ans += cur

                n = cur
            # divide till n is 0
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