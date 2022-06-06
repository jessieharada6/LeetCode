class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        n = len(isConnected[0])
        connection = m
        
        uf = UF(connection)
        
        for i in range(m):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.countNodes()

# more efficient version
class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        # self.size = [1 for _ in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP == rootQ:
            return
        
        self.parent[rootQ] = rootP
        self.count -= 1
            
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ
    
    def countNodes(self):
        return self.count

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]
        connections = 0
        
        def traverse(node):                 # node is like outer loop
            if visited[node]:
                return
            
            visited[node] = True
                                            # i is like inner loop
            for i in range(n):              # not isConnected[node] -> looking horizontally, it is job for dfs
                if not visited[i] and isConnected[node][i] == 1:    # not visited[i] equivalent to i != node
                    traverse(i)
        
        for c in range(n):
            if not visited[c]:
                connections += 1
                traverse(c)
        
        return connections