/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
 var checkSubarraySum = function(nums, k) {
    let runningSum = 0
    let map = new Map()
    // if the 1st index meets the condition
    map.set(0, -1)
    
    for (let i = 0; i < nums.length; i++) {
        runningSum += nums[i]
        if (k !== 0) runningSum %= k
        if (map.has(runningSum)) {
            if (i - map.get(runningSum) >= 2) {
                return true;
            }
        } else {
            map.set(runningSum, i)
        }
    }
    
    return false;
};