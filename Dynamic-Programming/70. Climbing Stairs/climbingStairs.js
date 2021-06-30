/**
 * @param {number} n
 * @return {number}
 */
// Time complexity: O(n)
// Space complexity: O(n)
var climbStairs = function (n) {
    let dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    dp[1] = 1;

    for (let i = 2; i < n + 1; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
};

/**
 * @param {number} n
 * @return {number}
 */
// Time complexity: O(n)
// Space complexity: O(n)
var climbStairs = function (n) {
    let step1 = 1;
    let step2 = 1;

    for (let i = 2; i < n + 1; i++) {
        let currentStep = step1 + step2;
        step1 = step2;
        step2 = currentStep;
    }

    return step2;
};