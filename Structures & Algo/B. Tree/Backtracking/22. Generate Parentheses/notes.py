# pure backtrack - all possibility
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paths = []
        p = []
        for i in range(n):
            p.append("(")
            p.append(")")
        used = [False for _ in range(n * 2)]
        print(p)
        
        def traverse(index, path):
            if len(path) == n * 2:
                paths.append(["".join(path)])
                return
            
            for i in range(n * 2):
                if used[i]: continue
                    
                used[i] = True
                path.append(p[i])
                traverse(i, path)
                path.pop()
                used[i] = False
        
        traverse(0, [])
        print(paths)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paths = []
        
        def traverse(index, path):
            if len(path) == n * 2:
                paths.append(["".join(path)])
                return
            
            for choice in ["(", ")"]:
                path.append(choice)
                traverse(index + 1, path)
                path.pop()
        
        traverse(0, [])
        print(paths)