class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [0] * n
        p2 = p3 = p5 = 0
        a = b = c = 1
        
        for i in range(n):
            ans[i] = min(a, b, c)

            if a == ans[i]:
                a = ans[p2] * 2
                p2 += 1
            if b == ans[i]:
                b = ans[p3] * 3
                p3 += 1
            if c == ans[i]:
                c = ans[p5] * 5
                p5 += 1
            
        return ans[-1]