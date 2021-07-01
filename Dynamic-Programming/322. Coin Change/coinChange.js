/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
    let dp = new Array(amount + 1).fill(amount + 1);
    let n = dp.length;
    dp[0] = 0;

    for (let i = 1; i < n; i++) {
        for (const coin of coins) {
            if (i - coin >= 0) {
                dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
            }
        }
    }

    return dp[n - 1] === amount + 1 ? -1 : dp[n - 1];
};