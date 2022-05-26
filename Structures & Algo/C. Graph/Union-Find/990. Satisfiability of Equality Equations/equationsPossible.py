class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)             # 26 letters 
        for e in equations:
            if e[1] == "=":
                uf.union(ord(e[0]) - 97, ord(e[3]) - 97)
       
        for e in equations:
            if e[1] == "!":
                if uf.connected(ord(e[0]) - 97, ord(e[3]) - 97):
                    return False 
        return True

class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.weight = [1 for _ in range(n)]
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if self.weight[p] > self.weight[q]:
            self.parent[rootQ] = self.parent[rootP]
            self.weight[rootP] += self.weight[rootQ]
        else:
            self.parent[rootP] = self.parent[rootQ]
            self.weight[rootQ] += self.weight[rootP]
        
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        return rootP == rootQ