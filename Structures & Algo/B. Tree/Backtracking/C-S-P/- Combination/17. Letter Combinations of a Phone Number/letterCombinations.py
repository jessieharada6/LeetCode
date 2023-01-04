class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        def dfs(path, i):
            if i == len(digits):
                ans.append(path)
                return
            
            # 循环字典里的value, 
            # i = 1时 循环填入第一个数字 
            # i = 2时 循环填入第二个数字（此时第一个数字已经填好）
            for c in dict[digits[i]]: 
                dfs(path + c, i + 1)

        
        dfs("", 0)
        return ans

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        vis = [False] * len(digits)
        ans = []
        if digits == "": return ans

        def dfs(path, i, vis):
            if i == len(digits):
                ans.append(path)
                return
            
            for j in range(i, len(digits)):
                if not vis[j]:
                    vis[j] = True
                    for c in dict[digits[j]]:
                        dfs(path + c, i + 1, vis)
                    vis[j] = False
            
        dfs("", 0, vis)
        return ans

       