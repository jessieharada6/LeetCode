class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [0] * n
        ans[0] = 1
        
        p2, p3, p5 = 0, 0, 0
        for idx in range(1, n):
            a = ans[p2] * 2
            b = ans[p3] * 3
            c = ans[p5] * 5
            
            num = min(a, b, c)
            ans[idx] = num
            
            if num == a: p2 += 1
            if num == b: p3 += 1
            if num == c: p5 += 1
                
        return ans[-1]