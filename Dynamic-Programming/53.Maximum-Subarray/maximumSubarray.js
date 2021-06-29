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