/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
 var numDistinct = function(s, t) {
    let m = t.length;
    let n = s.length;
    
    if (m === n && s == t) return 1;
    if (n < m) return 0;
    
    let dp = new Array(m + 1);
    for (let i = 0; i < m + 1; i++) {
        dp[i] = new Array(n + 1).fill(0);
    }
    
    for (let i = 0; i < n + 1; i++) {
        dp[0][i] = 1;
    }
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (s[j] === t[i]) {
                dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j];
            } else {
                dp[i + 1][j + 1] = dp[i + 1][j];
            }
        }
    }
    
    // dp[col][row]
    return dp[m][n]
};