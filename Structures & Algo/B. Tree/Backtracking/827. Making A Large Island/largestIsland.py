class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        largest_island = 0
        islands_cnt = collections.defaultdict(int)
        islands = 2
        visited = [[False] * n for _ in range(n)]

        # 算出目前拥有的岛屿数量
        def count_islands(row, col, islands):
            if row < 0 or col < 0 or row >= n or col >= n or grid[row][col] == 0 or visited[row][col]:
                return
            
            visited[row][col] = True
            grid[row][col] = islands
            islands_cnt[grid[row][col]] += 1
            for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                count_islands(r, c, islands)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    count_islands(i, j, islands) #注意：相连岛屿是一个岛
                    islands += 1 # 增加一个岛
        
        # 算出把海变成岛屿后的岛屿数量
        def get_islands(row, col):
            if 0 <= row + 1 < n:
                cnt_book[grid[row + 1][col]] = islands_cnt[grid[row + 1][col]]
            if 0 <= row - 1 < n:
                cnt_book[grid[row - 1][col]] = islands_cnt[grid[row - 1][col]]
            if 0 <= col + 1 < n:
                cnt_book[grid[row][col + 1]] = islands_cnt[grid[row][col + 1]]
            if 0 <= col - 1 < n:
                cnt_book[grid[row][col - 1]] = islands_cnt[grid[row][col - 1]]

        for i in range(n):
            for j in range(n):
                cnt = 0
                cnt_book = collections.defaultdict(int)
                if grid[i][j] == 0:
                    get_islands(i, j)
                    # print("cnt", cnt_book)
                    for k, v in cnt_book.items():
                        cnt += v
                    # print(cnt)
                    largest_island = max(largest_island, cnt + 1)
        
        return largest_island if largest_island != 0 else n * n