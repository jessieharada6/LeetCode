/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    let rob1 = 0;
    let rob2 = 0;

    for (let i = 0; i < nums.length; i++) {
        // compare 3 values, r1 ,r2 and num each time
        // accumulated max so far with rules obeyed
        let curMax = Math.max(rob1 + nums[i], rob2);
        // console.log(i, rob1 + nums[i], rob1, rob2, curMax)
        // rob1 records the max at the time of [i-2]
        rob1 = rob2;
        // rob2 records the max before the current [i]
        rob2 = curMax
    }

    return rob2;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    let rob1 = 0;
    let rob2 = 0;

    for (const num of nums) {
        let currentMax = Math.max(rob1 + num, rob2);
        rob1 = rob2;
        rob2 = currentMax;
    }

    return rob2;
};