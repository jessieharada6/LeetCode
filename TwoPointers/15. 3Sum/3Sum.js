/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
    let result = [];
    if (nums.length < 3) return result;

    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length; i++) {
        // if the smallest number is > 0, forget about it
        if (nums[i] > 0) break;
        // if the current nums[i] is the same as nums[i - 1]      
        // means there is a combination added to the array, skip
        if (i > 0 && nums[i - 1] === nums[i]) {
            continue;
        }

        // two sum II - two pointers     
        let l = i + 1;
        let r = nums.length - 1;

        while (l < r) {
            let sum = nums[i] + nums[l] + nums[r];
            if (sum === 0) {
                result.push([nums[i], nums[l], nums[r]]);

                // move pointers ahead   

                // 1. for case [-2, -2, 0, 0, 2, 2] to avoid repetition
                while (l < r && nums[l] === nums[l + 1]) {
                    l++;
                }
                while (l < r && nums[r] === nums[r - 1]) {
                    r--;
                }
                // 2. can't break like two sum II
                // as two sum II only has exactly one solution
                // this logic goes after the two while loop above
                // for case [-2, 0, 1, 1, 2]
                // at -2, if l and r moves then will be at 1 and 1
                // now nums[r] === nums[r - 1], then r will move
                // and now r === l will break out the loop
                l++;
                r--;

            }
            if (sum > 0) {
                r--;
            }
            if (sum < 0) {
                l++;
            }
        }
    }

    return result;
};