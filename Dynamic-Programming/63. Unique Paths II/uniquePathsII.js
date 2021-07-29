/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
    let m = obstacleGrid[0].length;
    let dp = new Array(m).fill(0);
    dp[0] = 1;

    for (const grid of obstacleGrid) {
        for (let i = 0; i < grid.length; i++) {
            // check if it's 1 including at index 0
            if (grid[i] === 1)
                dp[i] = 0;
            // if not, dp[0] = 1 by default
            // check the inner values
            else if (i > 0)
                // update based on the previous row
                dp[i] += dp[i - 1];
        }
        console.log(dp)
    }

    return dp[m - 1];
};


/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
 var uniquePathsWithObstacles = function(obstacleGrid) {
    let n = obstacleGrid.length;
    let m = obstacleGrid[0].length;
    
    let dp = new Array(m).fill(0);
    dp[0] = 1;
    
    for (let i = 0; i < n; i++){
        for (let j = 0; j < m; j++) {
            if (obstacleGrid[i][j] === 1) {
                // 1. first element in the row:
                // for every first element for every row
                // it is either 0 (with hurdle) or 1 (without hurdle)
                // 2. the rest of the elements with hurdle:
                // it's always 0 with hurdle
                dp[j] = 0;
            } else if (j > 0) {
                // the rest of the elements without hurdle:
                // increment once moving to the second element of every row (without hurdle)
                dp[j] += dp[j - 1];
            }
        }
    }
    
    return dp[m - 1];
};
