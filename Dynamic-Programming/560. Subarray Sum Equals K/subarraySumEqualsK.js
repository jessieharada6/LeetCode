/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var subarraySum = function(nums, k) {
    // sum[1:3] = sum[0:3] - sum[0:0] (inclusive)
    let map = new Map();
    // base case when sum is 0, it appears once
    // take into consideration of 0 index
    map.set(0, 1);
    let sum = 0, result = 0;
    
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        if (map.has(sum - k)) {
            result += map.get(sum - k);
        } 
        map.set(sum, (map.get(sum) || 0) + 1);
    }
    
    return result;
};