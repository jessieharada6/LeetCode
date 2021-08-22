/**
 * @param {string} s
 * @return {number}
 */
 var longestPalindromeSubseq = function(s) {
    let n = s.length;
    let dp = new Array(n);
    for (let i = 0; i < n; i++) {
        dp[i] = new Array(n).fill(0)
    }
    
    for (let i = n - 1; i >= 0; i--){
        dp[i][i] = 1;
        for (let j = i + 1; j < n; j++) {
            if (s[i] === s[j]) {
                dp[i][j] = 2 + dp[i + 1][j - 1];
            } else {
                dp[i][j] = Math.max(dp[i][j - 1], dp[i + 1][j])
            }
        }
    }
    
    return dp[0][n - 1]
};