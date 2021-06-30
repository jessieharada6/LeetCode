/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    return Math.max(nums[0], robHouse(nums, 0, nums.length - 2), robHouse(nums, 1, nums.length - 1));
};

function robHouse(nums, start, end) {
    let rob1 = 0;
    let rob2 = 0;

    for (let i = start; i <= end; i++) {
        let currentMax = Math.max(rob1 + nums[i], rob2);
        rob1 = rob2;
        rob2 = currentMax;
    }

    return rob2;
}