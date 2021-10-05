/**
 * @param {string} s
 * @return {number}
 */
 var minimumMoves = function(s) {
    let output = 0;
    let index = 0;
    
    while (index < s.length) {
        if (s[index] === "X") {
            output += 1;
            index += 3;
        } else {
            index += 1;
        }
    }
    
    return output;
};