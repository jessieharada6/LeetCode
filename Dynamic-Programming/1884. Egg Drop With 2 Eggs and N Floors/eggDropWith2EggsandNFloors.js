/**
 * @param {number} n
 * @return {number}
 */

// Time complexity: O(n^2)
// Space complexity: O(1)
var twoEggDrop = function (n) {
    let count = 0;
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            count++;
            if (count === n) {
                return i;
            }
        }
    }
};

/**
 * @param {number} n
 * @return {number}
 */
// Time complexity: O(1)
// Space complexity: O(1)
var twoEggDrop = function (n) {
    // let a = sqrt(1 + 8 * n)
    // let b = (a - 1) / 2
    // let c = ceil(b)
    return Math.ceil(Math.sqrt(1 + 8 * n) - 1) / 2;
};