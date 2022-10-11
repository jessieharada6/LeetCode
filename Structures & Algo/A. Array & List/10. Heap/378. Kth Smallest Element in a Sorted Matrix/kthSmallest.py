class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i, m in enumerate(matrix):
            heappush(heap, (m[0], i, 0))
        
        ans = 0
        while heap and k > 0:
            val, i, j = heappop(heap)
            ans = val
            k -= 1
            
            if j + 1 < len(matrix):
                heappush(heap, (matrix[i][j + 1], i, j + 1))
        
        return ans