var countVowelStrings = function (n) {
    // base case n = 1, it is [1, 1, 1, 1, 1]
    let dp = new Array(5).fill(1);

    // seen as n - 1, as it starts from 0
    for (let i = 1; i < n; i++) {
        for (let j = 1; j < dp.length; j++) {
            dp[j] = dp[j - 1] + dp[j];
        }
    }

    return dp.reduce((a, b) => a + b);
}