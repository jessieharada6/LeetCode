var numTeams = function (rating) {
    let result = 0;

    for (let i = 1; i < rating.length - 1; i++) {
        let leftL = 0, leftG = 0, rightL = 0, rightG = 0;
        for (let j = 0; j <= i - 1; j++) {
            if (rating[j] < rating[i]) {
                leftL++;
            } else {
                leftG++;
            }
        }

        for (let j = i + 1; j < rating.length; j++) {
            if (rating[j] < rating[i]) {
                rightL++;
            } else {
                rightG++;
            }
        }
        result += leftL * rightG + leftG * rightL;
    }

    return result;
}