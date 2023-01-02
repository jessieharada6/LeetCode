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
