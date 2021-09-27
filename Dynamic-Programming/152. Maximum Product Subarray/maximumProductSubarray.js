/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxProduct = function(nums) {
    let curMax = nums[0];
    let curMin = nums[0];
    let max = nums[0];
    
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < 0) {
            let temp = curMax;
            curMax = curMin;
            curMin = temp;
        }
        
        curMax = Math.max(curMax * nums[i], nums[i]);
        curMin = Math.min(curMin * nums[i], nums[i]);
        max = Math.max(curMax, max);
    }
    
    return max;
};