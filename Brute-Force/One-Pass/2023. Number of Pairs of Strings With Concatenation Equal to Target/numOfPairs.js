/**
 * @param {string[]} nums
 * @param {string} target
 * @return {number}
 */
// brute force
 var numOfPairs = function(nums, target) {
    let output = 0;
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (nums[i] + nums[j] === target && j !== i) {
                output += 1
            }  
        }
    }
    
    return output;
};

// Map
/**
 * @param {string[]} nums
 * @param {string} target
 * @return {number}
 */
 var numOfPairs = function(nums, target) {
    let output = 0;
    
    let map = new Map();
    for (let num of nums) {
        map.set(num, (map.get(num) || 0) + 1);
    }
    
    for (let i = 0; i < target.length; i++) {
        // split target
        let prefix = target.substring(0, i);
        let suffix = target.substring(i, target.length);
        
        // calculate output
        if (map.has(prefix) && map.has(suffix)) {
            if (prefix === suffix) {
                output += map.get(prefix) * (map.get(suffix) - 1);
            } else {
                output += map.get(prefix) * map.get(suffix);
            }
        }
        
    }
    
    return output;
};