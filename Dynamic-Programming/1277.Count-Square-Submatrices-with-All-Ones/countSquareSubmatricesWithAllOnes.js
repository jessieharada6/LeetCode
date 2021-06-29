var countSquares = function (matrix) {
    let result = 0;

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] > 0 && i > 0 && j > 0) {
                matrix[i][j] += Math.min(
                    matrix[i][j - 1], matrix[i - 1][j],
                    matrix[i - 1][j - 1])
            }
            result += matrix[i][j];
        }
    }

    return result;
};