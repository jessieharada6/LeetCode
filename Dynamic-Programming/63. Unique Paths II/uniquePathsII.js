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