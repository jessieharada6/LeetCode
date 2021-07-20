// same logic as 1143. Longest Common Subsequence

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
// Time Complexity: O(m * n)
var minDistance = function (word1, word2) {
    let dp = Array(word1.length + 1);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = Array(word2.length + 1).fill(0);
    }

    for (let i = word1.length - 1; i >= 0; i--) {
        for (let j = word2.length - 1; j >= 0; j--) {
            if (word1[i] === word2[j]) {
                dp[i][j] = 1 + dp[i + 1][j + 1]
            } else {
                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
            }
        }
    }

    return word1.length + word2.length - dp[0][0] * 2;
};
