class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        res=[]
        for i in range(len(s)):
            if s[i] in ('+','-','*'):
                left=self.diffWaysToCompute(s[:i])
                right=self.diffWaysToCompute(s[i+1:])
                for l in left:
                    for r in right:
                        l = int(l)
                        r = int(r)
                        if s[i] == "+":
                            res.append(l + r)
                        elif s[i] == "-":
                            res.append(l - r)
                        elif s[i] == "*":
                            res.append(l * r)
                        
        if len(res) > 0:
            return res
        
        return [s]     