/**
 * @param {number[]} nums
 * @return {number}
 */
 var maximumDifference = function(nums) {
    let output = Number.NEGATIVE_INFINITY;
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] < nums[j]) {
                output = Math.max(output, nums[j] - nums[i]);
            }
        }
    }
    
    return output === Number.NEGATIVE_INFINITY ? -1 : output;
};