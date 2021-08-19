/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
 var wordBreak = function(s, wordDict) {
    let n = s.length;
    let dp = new Array(n + 1).fill(false);
    dp[0] = true;
    
    let maxLen;
    for (const word in wordDict) {
        maxLen = Math.max(maxLen, word.length);
    }
    
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            if (i - j > maxLen) {
                continue;
            }
            if (dp[j] && wordDict.includes(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    
    return dp[n];
};