class Solution:
    def minimumDeletions(self, s: str) -> int:
        # total = 0
        # for x in s:
        #     if x is "a": total += 1
        
        # # 在左边删除b 右边删除a
        # res = total
        # for divider in range(len(s)):
        #     if s[divider] is "a":
        #         total -= 1
        #     else:
        #         total += 1
        #     res = min(res, total)
        # return res

        n = len(s)
        # 用前缀和算出a的数量
        prefix = [0] * n if s[0] is not "b" else [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1]
            if s[i] is "b": prefix[i] = prefix[i - 1] + 1
        
        @cache
        def dfs(i):
            if i < 0: return 0

            if s[i] is "a": 
                return min(prefix[i], dfs(i - 1) + 1) #当前是a 选a，prefix[i]需要改变的数量 不选a，改变a成b

            return dfs(i - 1) # 当前是b 什么也不用做

        return dfs(n - 1) # 从右边看向左边 右边应该都是b
