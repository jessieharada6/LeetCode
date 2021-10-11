/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
 var construct2DArray = function(original, m, n) {
    let output = [];
    
    if (m * n !== original.length)
        return [];
    
    for (let i = 0; i < m; i++) {
        output.push([]);
        for (let j = 0; j < n; j++) {
            output[i][j] = original[i * n + j];
        }
    }
    
    return output;
};