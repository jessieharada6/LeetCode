class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def getTrailingZeros(n):
            zeros = 0
            while n != 0:
                current = n // 5
                zeros += current
                n = current
            return zeros
        
        def getRange(left):
            l = 0
            r = int(10e9)
            i = -1
            while l <= r:
                m = l + (r - l) // 2
                if getTrailingZeros(m) > k:
                    r = m - 1
                elif getTrailingZeros(m) < k:
                    l = m + 1
                else:
                    i = m
                    if left:
                        r = m - 1
                    else:
                        l = m + 1
            return i
        
        l = getRange(True)
        r = getRange(False)
        
        return r - l + 1 if l != -1 and r != -1 else 0
        

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