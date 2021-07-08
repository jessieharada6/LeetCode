/**
 * @param {number[]} nums
 * @return {boolean}
 */
// Time Complexity: O(n)
// Space complexity: O(1)
var canJump = function (nums) {
    let n = nums.length - 1;
    // goal is initially 0
    let goal = 0;

    for (let i = n; i >= 0; i--) {
        // i + nums[i] 
        // stands on the current position (i) with current maximum steps (nums[i])
        // can i jump towards the goal (here -> goal)
        if (i + nums[i] >= goal) {
            goal = i;
        }
    }

    return goal === 0 ? true : false;
};