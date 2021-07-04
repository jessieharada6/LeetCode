/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function (nums) {
    let count = 0;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < nums[i - 1]) {
            // important to make sure if nums[i] = nums[i - 2]
            // press nums[i - 1] down
            if (i === 1 || nums[i] >= nums[i - 2]) {
                nums[i - 1] = nums[i];
                count++;
            } else {
                // deal with (nums[i] < nums[i - 2])
                nums[i] = nums[i - 1];
                count++;
            }
        }
    }

    return count <= 1;
};
