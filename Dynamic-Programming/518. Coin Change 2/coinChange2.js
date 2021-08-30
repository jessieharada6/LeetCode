var change = function(amount, coins) {
    let arr = Array(amount + 1).fill(0);
    arr[0] = 1;
    
    for (const coin of coins) {
        for (let i = 1; i < arr.length; i++) {
            if (i - coin >= 0) {    
                // arr[i - coin] choose the coin
                // arr[i] not choose the coin, stay as current amount
                arr[i] = arr[i - coin] + arr[i];
            } 
        }
    }
    
    // console.log(arr);
    return arr[arr.length - 1];
};

/**
 * @param {number} amount
 * @param {number[]} coins
 * @return {number}
 */
 var change = function(amount, coins) {
    let dp = new Array(amount + 1).fill(0)
    dp[0] = 1
    
    for (const coin of coins) {
        for (let i = 1; i <= amount; i++) {
            if (i - coin >= 0) {
                dp[i] = dp[i - coin] + dp[i]
            }
        }
    }
    
    return dp[amount]
};

