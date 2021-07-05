/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
    let count = 0;
    for (let i = 0; i < s.length; i++) {
        // odd
        helper(s, i, i);
        // even
        helper(s, i, i + 1);
    }

    return count;

    function helper(s, l, r) {
        // for every single char ("a") or even ("bb"), 
        // it will definitely go in for the first time
        while (l >= 0 && r < s.length && s.charAt(l) === s.charAt(r)) {
            count++;
            l--;
            r++;
        }
        // once s.charAt(l) !== s.charAt(r), 
        // while loop ends, i moves to the next index
    }
};