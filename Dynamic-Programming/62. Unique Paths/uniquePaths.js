/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
    let dp = new Array(n).fill(1);

    for (let i = 1; i < m; i++) {
        for (let j = 1; j < dp.length; j++) {
            dp[j] = dp[j - 1] + dp[j];
        }
    }

    return dp[n - 1];
};