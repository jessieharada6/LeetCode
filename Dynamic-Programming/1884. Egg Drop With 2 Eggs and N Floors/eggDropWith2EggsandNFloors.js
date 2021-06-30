/**
 * @param {number} n
 * @return {number}
 */

// Time complexity: O(n^2)
// Space complexity: O(1)
var twoEggDrop = function (n) {
    if (n === 1) return n;

    let count = 1;
    for (let i = 2; i < n + 1; i++) {
        for (let j = 0; j < i; j++) {
            count += 1;
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
    return Math.ceil(Math.sqrt(1 + 8 * n) - 1) / 2;
};