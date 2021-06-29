var canPartition = function (nums) {
    let sum = nums.reduce((a, b) => a + b);
    if (sum % 2) return false;

    let target = sum / 2;
    let dp = new Set();
    dp.add(0);

    for (const num of nums) {
        let newDP = new Set();
        for (const t of dp) {
            newDP.add(t);
            newDP.add(t + num);
        }
        dp = newDP;
    }

    return dp.has(target);
};