
/**
 * @param {string} s
 * @return {string}
 */
// Time Complexity: O(n ^ w)
// Space Complexity: O(n)
var longestPalindrome = function (s) {
    let maxLength = 0;
    let lower = 0;
    let upper = 0;

    for (let i = 0; i < s.length; i++) {
        // odd string 'bab'
        helper(s, i, i);
        // even string 'bb'
        helper(s, i, i + 1);
    }

    return s.substring(lower, upper);

    // focus on one char, expand the index to the two sides
    function helper(s, l, r) {
        while (l >= 0 && r < s.length && s.charAt(l) === s.charAt(r)) {
            l--;
            r++;
        }

        // find the max length within the 
        // as l will get reduce one more time when it comes out of the while loop
        // so lower bound must be l + 1
        // r won't matter, as substring is like [l, r)
        // [l + 1, r]
        if (maxLength < r - (l + 1)) {
            maxLength = r - (l + 1);
            lower = l + 1;
            upper = r;
        }
    }
};


/**
 * @param {string} s
 * @return {string}
 */
// Time Complexity: O(n ^ 3)
// Space Complexity: O(n)
// The key is not to actually swap the values at the helper function 
// Use .charAt to check if the string character of two ends is a match, and go closer towards each other
// s.substring is very expensive, as it always generates a new string 
var longestPalindrome = function (s) {
    let palindrom = ""
    for (let i = 0; i < s.length; i++) {
        for (let j = 0; j <= i; j++) {
            let sub = s.substring(j, i + 1);
            if (helper(sub)) {
                if (palindrom.length < sub.length) {
                    palindrom = sub;
                }
            }
        }
    }

    return palindrom;
};

function helper(s) {
    let l = 0;
    let r = s.length - 1;
    while (l < r) {
        if (s.charAt(l) !== s.charAt(r)) {
            return false;
        }
        l++;
        r--;
    }
    return true;
}