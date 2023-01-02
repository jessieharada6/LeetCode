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

       