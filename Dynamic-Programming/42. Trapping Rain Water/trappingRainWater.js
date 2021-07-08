/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
    let n = height.length;
    let l = 0, maxL = height[0];
    let r = n - 1, maxR = height[n - 1];
    let water = 0;

    while (l < r) {
        if (maxL < maxR) {
            l += 1;
            maxL = Math.max(maxL, height[l]);
            water += (maxL - height[l]);
        } else {
            r -= 1;
            maxR = Math.max(maxR, height[r]);
            water += (maxR - height[r]);
        }
    }

    return water;
};



/**
 * @param {number[]} height
 * @return {number}
 */
// Time complexity: O(n^2)
// Space Complexity: O(n)
var trap = function (height) {
    let n = height.length;
    let maxLeft = new Array(n).fill(0);
    let maxRight = new Array(n).fill(0);
    let lr = new Array(n).fill(0);
    let sum = 0;

    // base case
    maxLeft[0] = 0;
    maxRight[n - 1] = 0;

    // get max left for the current number
    for (let i = 1; i < height.length; i++) {
        for (let j = 0; j < i; j++) {
            if (maxLeft[i] < height[j]) {
                maxLeft[i] = height[j];
            }
        }
    }

    // get max right for the current number
    for (let i = n - 2; i >= 0; i--) {
        for (let j = n - 1; j > i; j--) {
            if (maxRight[i] < height[j]) {
                maxRight[i] = height[j];
            }
        }
    }

    // get min based on max left and max right
    for (let i = 0; i < n; i++) {
        lr[i] = Math.min(maxLeft[i], maxRight[i]);
    }

    // min(maxLeft, maxRight) - height[i]
    for (let i = 0; i < n; i++) {
        let current = lr[i] - height[i];
        if (current > 0) {
            sum += current;
        }
    }

    return sum;
};