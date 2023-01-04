class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(path, i):
            print(path, i)
            if i == len(s) and len(path) == len(s) + 3:
                ans.append(path)
                return
            
            for j in range(i, len(s)):
                part = s[i:j + 1]
                partInInt = int(part)
                if part[0] == "0" and len(part) > 1: continue
                if partInInt <= 255:
                    if j + 1 != len(s):
                        dfs(path + part + ".", j + 1)
                    else:
                        dfs(path + part, j + 1)
        
        dfs("", 0)
        return ans


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