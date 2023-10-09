class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i):
            if i <= 0: # i = 0: current i is used up; i < 0: i < zero or one
                return 1 if i == 0 else 0

            return (dfs(i - zero) + dfs(i - one)) % MOD

        res = 0
        for i in range(low, high + 1):
           res = (res + dfs(i)) % MOD # modulus on final res 
           # res += dfs(i) % MOD will not work as it only modulus on dfs(i) in which res will exceed 
        return res

