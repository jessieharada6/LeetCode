class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        distances = [[0 for _ in range(m)] for _ in range(n)]
        
        longest_distance = m - 1 + n - 1
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    up = distances[i - 1][j] if (i > 0) else longest_distance
                    left = distances[i][j - 1] if (j > 0) else longest_distance
                    distances[i][j] = min(up, left) + 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if mat[i][j] != 0:
                    down = distances[i + 1][j] if (i < n - 1) else longest_distance
                    right = distances[i][j + 1] if (j < m - 1) else longest_distance
                    distances[i][j] = min(min(down, right) + 1, distances[i][j])
                    
        return distances