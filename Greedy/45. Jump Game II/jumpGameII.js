/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function (nums) {
    // max: max jump, jump: counter, currentMax: current max jump at the current position 
    let max = 0, jumps = 0, currentMax = 0;

    // i < nums.length - 1 prevents jumps to go out of the boundary
    // if i < nums.length - when i === currentMax at nums.length - 1, we will jump again
    for (let i = 0; i < nums.length - 1; i++) {
        max = Math.max(max, i + nums[i]);
        if (currentMax === i) {
            jumps++;
            currentMax = max;
        }
    }

    return jumps;
};