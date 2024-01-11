class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(m):
            cnt = 0
            for row in matrix:
                cnt += bisect_right(row, m)
            print(cnt, m)
            return cnt >= k
        
        l = matrix[0][0] - 1
        r = matrix[-1][-1]
        
        while l + 1 < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        return r

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(m):
            cnt = 0
            col = n - 1
            for row in matrix:
                while col >= 0 and row[col] > m:
                    col -= 1
                cnt += col + 1
            return cnt >= k
        
        l = matrix[0][0] - 1
        r = matrix[-1][-1]
        
        while l + 1 < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        return r
         