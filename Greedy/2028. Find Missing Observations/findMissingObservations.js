/**
 * @param {number[]} rolls
 * @param {number} mean
 * @param {number} n
 * @return {number[]}
 */
 var missingRolls = function(rolls, mean, n) {
    let m = rolls.length;
    let total = mean * (m + n);
    let total_m = rolls.reduce((a, b) => a + b);
    let diff = total - total_m;
    
    // the diff can't be larger than n *6, as max of dice is 6
    // the diff can't be less than n, as min of dice of 1
    if (diff > n * 6 || diff < n) {
        return [];
    }
    
    // must use floor, otherwise values will round up
    let average = Math.floor(diff / n);
    let remaining = diff % n;
    // distribute average to output
    let output = new Array(n).fill(average);

    // evenly distribute the remaining nicely to the output
    for (let i = 0; i < remaining; i++) {
        output[i] += 1   
    }

    return output;
};