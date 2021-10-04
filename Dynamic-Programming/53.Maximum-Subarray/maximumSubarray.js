var maxSubArray = function (nums) {
    let currentMax = nums[0];
    let max = nums[0];

    if (nums.length === 1) return max;

    for (let i = 1; i < nums.length; i++) {
        currentMax = Math.max(nums[i], currentMax + nums[i]);
        max = Math.max(max, currentMax);
    }

    return max;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    let curMax = nums[0];
    let output = nums[0];
    
    for (let i = 1; i < nums.length; i++) {
        curMax = Math.max(nums[i], curMax + nums[i]);
        output = Math.max(curMax, output);
    }
    
    return output;
};