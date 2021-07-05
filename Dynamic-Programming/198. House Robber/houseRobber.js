/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    let rob1 = 0;
    let rob2 = 0;

    for (let i = 0; i < nums.length; i++) {
        let currentMax = Math.max(rob1 + nums[i], rob2);
        rob1 = rob2;
        rob2 = currentMax;
    }

    return rob2
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