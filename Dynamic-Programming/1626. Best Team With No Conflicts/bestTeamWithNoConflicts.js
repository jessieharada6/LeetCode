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
        // if same age
        if (a[0] === b[0]) {
            // return higher scores first
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



/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function (scores, ages) {
    let pairArr = scores.map((val, index) => [val, ages[index]]);
    //[score, age]
    pairArr.sort((a, b) => {
        if (a[1] === b[1]) {
            return b[0] - a[0];
        }
        return b[1] - a[1];
    })

    let newScore = [];
    for (const score of pairArr) {
        newScore.push(score[0]);
    }
    let n = newScore.length;

    // can't let dp = newScore
    // as it creates a shallow copy
    // it will modify values in  newScore when we modify dp
    let dp = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        dp[i] = newScore[i];
    }

    for (let i = 0; i < n; i++) {
        let s = newScore[i];
        for (let j = 0; j < i; j++) {
            // must consider =, 
            // for the same score, 
            // we want to compare the max
            if (s <= newScore[j]) {
                dp[i] = Math.max(dp[i], s + dp[j]);
            }
        }
    }

    return Math.max(...dp);
};