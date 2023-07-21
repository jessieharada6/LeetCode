class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10 ** 9 + 7
        f = [1, 2, 4]
        g = [1, 2, 4, 8]
        for _ in range(10 ** 5):
            f.append((f[-3] + f[-2] + f[-1]) % MOD)
            g.append((g[-4] + g[-3] + g[-2] + g[-1]) % MOD)
        
        ans = 1
        for ch, s in groupby(pressedKeys):
            length = len(list(s))
            if ch in "79":
                ans = ans * g[length - 1] % MOD
            else:
                ans = ans * f[length - 1] % MOD
            
            # ans = ans * (g[length - 1] if ch in "79" else f[length - 1]) % MOD
            
        return ans 





### group by

# class Solution:
#     def countTexts(self, pressedKeys: str) -> int:
        
#         group = []
#         for ch, s in groupby(pressedKeys):
#             group.append(list(s))
#             print(ch, len(list(s)), list(s))
#         print(group)
#         return 0

#output
# 2 0 []
# 3 0 []
# [['2', '2', '2'], ['3', '3']]

