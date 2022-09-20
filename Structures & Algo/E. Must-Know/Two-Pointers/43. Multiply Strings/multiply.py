class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                cur = int(num1[i]) * int(num2[j])
                
                p1, p2 = i + j, i + j + 1
                acc = cur + res[p2]
                res[p2] = acc % 10
                res[p1] += acc // 10
        
        ans = ''
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        
        print(res, i)
        while i < len(res):
            ans += str(res[i])
            i += 1
         
        print(ans)
        return ans if ans else "0"