/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
// count 1
 var longestOnes = function(nums, k) {
    let output = 0;
    let left = right = 0;
    let numT = numF = 0;
    
    // slide right
    while (right < nums.length) {
        if (nums[right] === 1) 
            numT++;
        else
            numF++;
        
        // if numF more than k
        // means we can't flip anymore
        // slide left
        while (numF > k) {
            if (nums[left] === 1) 
                numT--;
            else
                numF--;
            left++;
        }
        
        output = Math.max(output, right - left + 1);
        right++;
    }
    
    return output;
};