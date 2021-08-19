// S(2, 2)
// if obstacle:
//  return 0;
// else:
//  + option1 = S(1, 2)
//  + option2 = S(2, 1)
//  return option1 + option2

class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int sizeX = obstacleGrid[0].length;
        int sizeY = obstacleGrid.length;
        
        SlidingMatrix memo = new SlidingMatrix();
        memo.values = new int[sizeX];
        
        for (int y = 0; y < sizeY; y++) {
            for (int x = 0; x < sizeX; x++) {
                if (obstacleGrid[y][x] == 1) {
                    memo.feed(x, y, 0);
                } else {
                    if (x == 0 && y == 0) {
                        memo.feed(x, y, 1);
                    } else {
                        memo.feed(x, y, memo.get(x, y - 1) + memo.get(x - 1, y));
                    }
                }
            }
        }
        return memo.get(sizeX - 1, sizeY - 1);
    }
}

class SlidingMatrix {
    int[] values;
    
    int get(int x, int y) {
        if (y < 0 || x < 0) {
            return 0;
        }
        return values[x];
    }
    
    // setter
    void feed(int x, int y, int value) {
        values[x] = value;
    }
}

