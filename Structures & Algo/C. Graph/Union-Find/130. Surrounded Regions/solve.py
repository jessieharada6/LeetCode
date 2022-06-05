class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [0 for _ in range(n)]
        self.weight = [0 for _ in range(n)]
        for i in range(n):
            self.parent[i] = i      # all tree's root belongs to itself
            self.weight[i] = 1        # each tree's weight is one
        
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if self.weight[rootP] > self.weight[rootP]:
            self.parent[rootQ] = rootP
            self.weight[rootP] += self.weight[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.weight[rootQ] += self.weight[rootP]
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ
        
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        
        m = len(board)
        n = len(board[0])
        
        uf = UF(m * n + 1)          # 2d to 1d
        dummy = m * n
        
        # first and last column 
        for i in range(m):
            if board[i][0] == "O":
                uf.union(i * n + 0, dummy)
            if board[i][n - 1] == "O":
                uf.union(i * n + n - 1, dummy)
        
        # first and last row
        for i in range(n):
            if board[0][i] == "O":
                uf.union(i, dummy)
            if board[m - 1][i] == "O":
                uf.union(i + n * (m - 1), dummy)
        
        # for detecting the neighbours on a 2d element
        d = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O":          # if (i, j) = 0, find all neighbours 
                    for k in range(len(d)):     # if (i, j) = (1, 1), x, y will be (1, 0), (0, 1), (2, 1), (2, 2)
                        x = i + d[k][0]
                        y = j + d[k][1]
                        # print("x:", i, k, d[k][0], x)
                        # print("y:",j, k, d[k][1], y)
                        if board[x][y] == "O":  # if (x, y) = 0
                            uf.union(x * n + y, i * n + j)  # 2d to 1d, and union
                            # print(x * n + y, i * n + j, n, x, y)
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not uf.connected(dummy, i * n + j):
                    board[i][j] = "X"