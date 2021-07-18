/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    let map = new Map();
    for (let i = 0; i < nums.length; i++) {
        map.set(nums[i], i);
    }

    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i];
        if (map.has(diff) && map.get(diff) !== i) {
            return [map.get(diff), i];
        }
    }
};



/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
//Brute Force
var twoSum = function (nums, target) {
    let result = [];

    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i];
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[j] === diff) {
                result.push(i);
                result.push(j);
            }
        }
    }

    return result;
};