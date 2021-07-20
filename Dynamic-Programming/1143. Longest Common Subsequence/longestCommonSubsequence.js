/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
// bottom up approach
// Time Complexity: O(m * n)
var longestCommonSubsequence = function (text1, text2) {
    // init number of rows 
    let dp = new Array(text1.length + 1).fill(0);
    // init each row with value
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(text2.length + 1).fill(0)
    }

    for (let i = text1.length - 1; i >= 0; i--) {
        for (let j = text2.length - 1; j >= 0; j--) {
            if (text1[i] === text2[j]) {
                // common character - diagnomally 
                dp[i][j] = 1 + dp[i + 1][j + 1];
            } else {
                dp[i][j] = Math.max(dp[i][j + 1], dp[i + 1][j]);
            }
        }
    }

    // [
    // [ 3, 2, 1, 0 ],
    // [ 2, 2, 1, 0 ],
    // [ 2, 2, 1, 0 ],
    // [ 1, 1, 1, 0 ],
    // [ 1, 1, 1, 0 ],
    // [ 0, 0, 0, 0 ]
    // ]
    return dp[0][0];
};


