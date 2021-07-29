/**
 * @param {number} n
 * @param {number[]} cuts
 * @return {number}
 */
var minCost = function (n, cuts) {
    let memo = new Map();
    return dp(0, n);

    function dp(start, end) {
        let key = start + "-" + end;

        if (memo.has(key)) {
            return memo.get(key)
        }

        let canCut = false;
        let result = Infinity;

        for (const cut of cuts) {
            if (cut > start && cut < end) {
                canCut = true;
                result = Math.min(result, dp(start, cut) + dp(cut, end) + (end - start));
            }
        }

        if (canCut === false) {
            return 0;
        }

        memo.set(key, result);
        return result;
    }
};