/**
 * @param {number[]} nums
 * @return {number}
 */
 var arrayNesting = function(nums) {
    let visited = new Set();
    let max = 0;
    
    for (let i = 0; i < nums.length; i++) {
        let size = 0;
        for (let index = i; nums[index] >= 0; size++) {
            let currentIndex = nums[index];
            // visited
            nums[index] = -1;
            index = currentIndex;
        }

        max = Math.max(size, max);
    }
    
    return max;
};