class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        ans = [0] * n
        ans[0] = 1
        p = [0] * m
        
        for idx in range(1, n):
            num = inf
            for i in range(m):
                num = min(num, ans[p[i]] * primes[i])
            
            ans[idx] = num
            
            for i in range(m):
                if num == ans[p[i]] * primes[i]:
                    p[i] += 1
        
        return ans[-1]
                    
            
            
                 
            