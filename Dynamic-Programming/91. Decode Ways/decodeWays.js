var numDecodings = function (s) {
    let n = s.length;
    if (!s || n === 0) return 0;

    let dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    dp[1] = s.charAt(0) === "0" ? 0 : 1;

    for (let i = 2; i < dp.length; i++) {
        let option1 = parseInt(s.substring(i - 1, i));
        let option2 = parseInt(s.substring(i - 2, i));

        if (option1 >= 1 && option1 <= 9) {
            dp[i] += dp[i - 1];
        }
        if (option2 >= 10 && option2 <= 26) {
            dp[i] += dp[i - 2];
        }
    }
    return dp[n];
};