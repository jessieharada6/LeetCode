# 只用两个变量
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(path, open):
            if len(path) > n * 2: return
            if open == n and len(path) - open == n:
                ans.append(path)
                return
            
            # 这里也是有for loop 只是展开了 (, )两个
            dfs(path + "(", open + 1)
            if open > len(path) - open:
                dfs(path + ")", open)
        
        dfs("", 0)
        return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(path, o, c):
            if o > n or c > n: return
            if o == n and c == n:
                ans.append(path)
                return
            
            dfs(path + "(", o + 1, c)
            if c < o: # 需要先生成"("。在")"不够的情况下 再生成")"
                dfs(path + ")", o, c + 1)
        
        dfs("", 0, 0)
        return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paths = []

        def dfs(path, l, r):
            if l > n or r > n: return
            # print(l, r, path)
            if l == n and r == n:
                paths.append(path)
            
            # print(path, l, r)

            # path += "(" # 不可这样 这样每次必经这行 会多加(
            dfs(path + "(", l + 1, r) # 会被if l > n or r > n款住
            if l > r:
                # path += ")"
                dfs(path + ")", l, r + 1)

        dfs("", 0, 0)
        return paths

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(path, i, o, c):
            if i > n * 2: return
            if o == n and c == n:
                ans.append(path)
                return
            # 不需要i 因为有o和c作为树的指针
            dfs(path + "(", i + 1, o + 1, c)
            if c < o: 
                dfs(path + ")", i + 1, o, c + 1)
        
        dfs("", 0, 0, 0)
        return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paths = []
        
        def traverse(left, right, path):
            
            if left > n or right > n: return
            
            if left == n and right == n:
                paths.append("".join(path))
                return   
            
            if left < right: return
            
            path.append("(")
            traverse(left + 1, right, path)
            path.pop()
            
            path.append(")")
            traverse(left, right + 1, path)
            path.pop()
        
        traverse(0, 0, [])
        return paths
