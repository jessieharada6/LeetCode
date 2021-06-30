/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
// Time: O(n ^ 3)
// Memory: O(1).
var countSubstrings = function (s, t) {
    let result = 0;
    for (let i = 0; i < s.length; i++) {
        for (let j = 0; j < t.length; j++) {
            let diff = 0;
            for (let pos = 0; pos + i < s.length && pos + j < t.length; pos++) {
                if (s[pos + i] !== t[pos + j]) diff++;
                if (diff > 1) break;
                result += diff;
            }
        }
    }

    return result;
};