class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(s):
            return s and (s == "0" or s[0] != "0" and 0 <= int(s) <= 255) # s and 空串直接返回false,之后无法判断会报错

        n = len(s)
        paths = []
        def dfs(s, cnt, path) -> None:
            # if len(path) == n + 3: return # 加入s and 不会再溢出
            if cnt == 3: 
                if isValid(s):
                    paths.append(path + s)
                    return
                return
            

            for i in range(1, 4):
                cur = s[:i]
                if isValid(cur):
                    dfs(s[i:], cnt + 1, path + cur + ".")

        dfs(s, 0, "")
        return paths
        
        
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(path, i):
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
        paths = []
        def isValid(s):
            return s and 0 <= int(s) <= 255 and s[0] != "0" or s == "0"

        def dfs(path, input, cnt):
            if cnt == 3 and isValid(input):
                paths.append(path + input)
            
            for i in range(1, 4):
                if not isValid(input[:i]): break # 如果当前sliced的input不valid 整个ip都不行 直接重新加点
                dfs(path + input[:i] + ".", input[i:], cnt + 1) # 目前符合条件的input[:i] 拆分新的input[i:]
            
        dfs("", s, 0)
        return paths


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