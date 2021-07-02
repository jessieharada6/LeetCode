/**
 * @param {number[]} piles
 * @return {boolean}
 */

// Time complexity: O(n)
// Space complexity: O(n)
var stoneGame = function (piles) {
    let alex = 0;
    let lee = 0;

    while (piles.length) {
        alex += getMax(piles)[0];
        piles.splice(getMax(piles)[1], 1);

        lee += getMax(piles)[0];
        piles.splice(getMax(piles)[1], 1);
    }
    return alex > lee;
};

function getMax(piles) {
    let max = 0;
    let maxIndex = 0;
    for (let i = 0; i < piles.length; i++) {
        if (i === 0 || i === piles.length - 1) {
            max = Math.max(...piles);
            maxIndex = piles.indexOf(max);
        }
    }

    return [max, maxIndex]
}