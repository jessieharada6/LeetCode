class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # r: height, c: width
        r, c = len(mat), len(mat[0])
        integral_image = [[0 for _ in range(c)] for _ in range(r)]
        
        # build integral image: 
        for i in range(r):
            sum = 0
            for j in range(c):
                sum += mat[i][j]
                integral_image[i][j] = sum
                
                if i > 0:
                    integral_image[i][j] += integral_image[i - 1][j]
        
        print(integral_image)
        
        # compute block sum based on k range
        image = [[0 for _ in range(c)] for _ in range(r)] 
        
        for i in range(r):
            for j in range(c):
                min_row, max_row = max(0, i - k), min(r - 1, i + k)
                min_col, max_col = max(0, j - k), min(c - 1, j + k)
                
                # print("row", i, min_row, max_row, "col", j, min_col, max_col)
                
                image[i][j] = integral_image[max_row][max_col]
                
                if min_row > 0:
                    image[i][j] -= integral_image[min_row - 1][max_col]
                
                if min_col > 0:
                    image[i][j] -= integral_image[max_row][min_col - 1]
                
                if min_col > 0 and min_row > 0:
                    image[i][j] += integral_image[min_row - 1][min_col - 1]
        
        return image
                    
                    