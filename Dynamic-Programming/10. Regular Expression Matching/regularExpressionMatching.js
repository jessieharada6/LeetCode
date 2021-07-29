/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function (s, p) {
    let m = s.length;
    let n = p.length;
    let dp = new Array(m + 1)
    for (let i = 0; i < m + 1; i++) {
        dp[i] = new Array(n + 1).fill(false)
    }

    // for the first line
    dp[0][0] = true;
    // It is guaranteed for each appearance of the character '*', there will be a previous valid character to match. - so can start from index 2
    for (let i = 2; i < n + 1; i++) {
        // * represents the 0 element
        if (p[i - 1] === "*") dp[0][i] = dp[0][i - 2];
    }

    for (let i = 1; i < m + 1; i++) {
        for (let j = 1; j < n + 1; j++) {
            if (p[j - 1] === s[i - 1] || p[j - 1] === ".") {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p[j - 1] === "*") {
                // char+* = zero element
                if (dp[i][j - 2] === true) {
                    dp[i][j] = true;
                    // char at p[j - 2] = char at s[i - 1] or .
                    // * can be 1 or more elements
                } else if (p[j - 2] === s[i - 1] || p[j - 2] === ".") {
                    dp[i][j] = dp[i - 1][j]
                }
            }
        }
    }

    return dp[m][n];
};