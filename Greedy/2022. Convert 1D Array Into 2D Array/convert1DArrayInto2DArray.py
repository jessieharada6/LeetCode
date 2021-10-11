class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        output = [[0 for _ in range(n)] for _ in range(m)]
        
        if m * n != length:
            return []
        
        for i in range(m):
            for j in range(n):
                # key is here:
                # row increasing i * col n + col increasing j
                output[i][j] = original[i * n + j]
        
        return output
        