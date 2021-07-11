/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function (nums) {
    // max: max jump, jump: counter, currentPosition: current position
    let max = 0, currentPosition = 0, jumps = 0;

    // i < nums.length - 1 prevents jumps to go out of the boundary
    // if i < nums.length - when i === currentMax at nums.length - 1, we will jump again
    for (let i = 0; i < nums.length - 1; i++) {
        max = Math.max(nums[i] + i, max);
        if (currentPosition === i) {
            currentPosition = max
            jumps++;
        }
    }

    return jumps
};