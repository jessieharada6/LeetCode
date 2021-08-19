// S(x, y)
// S(2, 2)
// option1 = S(1, 2) ?
// option2 = S(2, 1) ?
// return Math.min(option1, option2) + grid[2][2]
class Solution {
    public int minPathSum(int[][] grid) {
        int sizeX = grid[0].length;
        int sizeY = grid.length;
        
        SlidingMatrix memo = new SlidingMatrix();
        memo.values = new int[sizeX];
        
        for (int y = 0; y < sizeY; y++) {
            for (int x = 0; x < sizeX; x++) {
                int solution = -1;
                solution = better(solution, memo.get(x - 1, y));
                solution = better(solution, memo.get(x, y - 1));
                solution = add(solution, grid[y][x]);
                memo.feed(x, y, solution);
            }
        }
        return memo.get(sizeX - 1, sizeY - 1);
    }
    
    private int better(int solution1, int solution2) {
        if (solution1 == -1 && solution2 == -1) {
            return -1;
        } else if (solution1 == -1) {
            return solution2;
        } else if (solution2 == -1) {
            return solution1;
        } else {
            return Math.min(solution1, solution2);
        }
    }
    
    private int add(int solution, int value){
        return solution == -1 ? value : solution + value;
    }
    
    class SlidingMatrix {
        int[] values;

        int get(int x, int y) {
            if (y < 0 || x < 0) {
                return -1;
            }
            return values[x];
        }

        // setter
        void feed(int x, int y, int value) {
            values[x] = value;
        }
    }
}

