/**
 * @param {number[]} stones
 * @return {boolean}
 */
 var stoneGameIX = function(stones) {
    count = new Array(3).fill(0);
    for (let s of stones) {
        count[s % 3] += 1
    }
    
    if (count[0] % 2 === 0 && count[1] * count[2] > 0)
        return true;
    if (count[0] % 2 === 1 && Math.abs(count[1] - count[2]) >= 3)
        return true;
    return false;
};