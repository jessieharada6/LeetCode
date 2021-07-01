/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
    let n = nums.length;
    let dp = new Array(n).fill(1);

    for (let i = 1; i < n; i++) {
        let point = nums[i];
        for (let j = 0; j < i; j++) {
            if (point > nums[j]) {
                // it is essential to use max to update the dp[i]
                // we want the largest current subsequence 
                // with example of [0, 1, 0, 3, 2, 2]
                //           dp is [1, 2, 1]
                // then at 3, 3 > 0, so dp[i] is 2
                // 3 is also > 1, so dp[i] should be 3 eventually
                dp[i] = Math.max(dp[j] + 1, dp[i]);
            }
        }
    }
    console.log(dp)

    // as we don't carry over the current max
    // for example [1,3,6,7,9,4,10,5,6]
    //     dp is   [ 1, 2, 3, 4, 5, 3, 6, 4, 5]
    return Math.max(...dp);
};