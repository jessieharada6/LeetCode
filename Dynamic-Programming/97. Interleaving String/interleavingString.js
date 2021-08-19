/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
 var isInterleave = function(s1, s2, s3) {
    let l1 = s1.length;
    let l2 = s2.length;
    let l3 = s3.length;
    
    if (l1 + l2 !== l3) {
        return false;
    }
    // same orders + same combinations of letters    
    
    let dp = new Array(l1 + 1);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(l2 + 1).fill(false);
    }
    
    dp[0][0] = true;
    
    for (let i = 1; i < dp[0].length; i++) {
        dp[0][i] = dp[0][i - 1] && (s2[i - 1] == s3[i - 1]);
    }
    
    for (let i = 1; i < dp.length; i++) {
        dp[i][0] = dp[i - 1][0] && (s1[i - 1] == s3[i - 1]);
    }
    
    for (let i = 1; i < dp.length; i++) {
        for (let j = 1; j < dp[0].length; j++) {
            dp[i][j] = 
                (dp[i - 1][j]&&(s1[i - 1] === s3[i + j - 1]))
                || (dp[i][j - 1] && (s2[j - 1] === s3[i + j - 1])) 
        }
    }
        
    return dp[l1][l2];
};