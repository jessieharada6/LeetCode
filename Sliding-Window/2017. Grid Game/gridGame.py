class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        output = math.inf
        
        n = len(grid[0])  
        prefix_sum_top = grid[0].copy()
        prefix_sum_bottom = grid[1].copy()
        
        #prefix sum for top and bottom
        for i in range(1, n):
            prefix_sum_top[i] += prefix_sum_top[i - 1]
            prefix_sum_bottom[i] += prefix_sum_bottom[i - 1]
        
        print(prefix_sum_top , prefix_sum_bottom)
        
        #calculate remaining
        for i in range(n):
            top = prefix_sum_top[-1] - prefix_sum_top[i]
            bottom = prefix_sum_bottom[i - 1] if i > 0 else 0
            # at each movement, robot 2 tries to maximise it
            robot2 = max(top, bottom)
            # minimise robot 2 points
            output = min(output, robot2)

        return output