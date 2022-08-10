# sieve of eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [1] * n
        count = 0
        
        for i in range(2, n):
            if isPrime[i]:
                count += 1
                for j in range(i * i, n, i):
                    isPrime[j] = 0
        
        return count