/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
 var minDistance = function(word1, word2) {
    let m = word1.length + 1;
    let n = word2.length + 1;
    let dp = new Array(n)
    for (let i = 0; i < n; i++) {
        dp[i] = new Array(m).fill(0);
    }
    
    for (let i = 1; i < m; i++) {
        dp[0][i] = dp[0][i - 1] + 1
    }
    
     for (let i = 1; i < n; i++) {
        dp[i][0] = dp[i - 1][0] + 1
    }
    
    for (let i = 1; i < n; i++) {
        for (let j = 1; j < m; j++) {
            if (word1[j - 1] === word2[i - 1]) {
                dp[i][j] = dp[i - 1][j - 1]
            } else {
                dp[i][j] = Math.min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1;
            }
        }
    }
    return dp[n - 1][m - 1];
};