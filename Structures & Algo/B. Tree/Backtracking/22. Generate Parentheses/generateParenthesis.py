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
