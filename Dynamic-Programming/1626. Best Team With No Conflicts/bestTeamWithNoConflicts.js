/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function (scores, ages) {
    // sort two arrays based on one array's updated positions
    let pairArr = ages.map((val, index) => [val, scores[index]]);
    // console.log(pairArr)
    pairArr.sort((a, b) => {
        if (a[0] === b[0]) {
            // if same age, higher scores go first
            return b[1] - a[1];
        }
        // descend age
        return b[0] - a[0];
    })

    let sortedScores = [];
    // let sortedAges = []
    for (const num of pairArr) {
        sortedScores.push(num[1]);
        // sortedAges.push(num[0]);
    }

    let max = 0;
    let dp = new Array(scores.length).fill(0);
    for (let i = 0; i < sortedScores.length; i++) {
        let score = sortedScores[i];
        dp[i] = score;
        for (let j = 0; j < i; j++) {
            if (sortedScores[j] >= score) {
                dp[i] = Math.max(dp[i], dp[j] + score);
            }
        }
        max = Math.max(dp[i], max);
    }

    return max;
};