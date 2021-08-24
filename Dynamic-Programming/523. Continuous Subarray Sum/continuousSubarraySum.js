/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
 var checkSubarraySum = function(nums, k) {
    let map = new Map();
    map.set(0, -1);
    let runningSum = 0;
    
    for (let i = 0; i < nums.length; i++) {
        runningSum += nums[i];
        if (k !== 0)
            runningSum %= k;
        
        if (map.has(runningSum)) {
            if (i - map.get(runningSum) > 1) {
                return true;
            }
        } else {
            map.set(runningSum, i);
        }
    }
    
    return false;

};