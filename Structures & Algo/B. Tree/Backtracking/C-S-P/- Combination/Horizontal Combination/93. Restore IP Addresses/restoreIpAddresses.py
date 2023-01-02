class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(path, i):
            if len(path) == len(s) + 3 and i == len(s): 
                ans.append(path)
                return
            
            for j in range(i, len(s)):
                if len(s[i:j + 1]) > 1 and s[i] == "0": continue
                if int(s[i:j + 1]) <= 255:
                    if j + 1 == len(s):
                        dfs(path + s[i:j + 1], j + 1) # 横向往右推动
                    else:
                        dfs(path + s[i:j + 1] + ".", j + 1) # 横向往右推动
        
        dfs("", 0)
        return ans