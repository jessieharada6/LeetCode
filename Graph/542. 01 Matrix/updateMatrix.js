/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
 var updateMatrix = function(mat) {
    let n = mat.length; 
    let m = mat[0].length; 

    // build columns
    let distances = new Array(n);
    // traverse to n
    for (let i = 0; i < n; i++) {
        distances[i] = new Array(m).fill(0);
    }
    
    let longestDistance = n - 1 + m - 1;
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if(mat[i][j] !== 0) {
                let up = (i > 0) ? distances[i - 1][j] : longestDistance;
                let left = (j > 0) ? distances[i][j - 1] : longestDistance;
                distances[i][j] = Math.min(up, left) + 1;
            }
        }
    }
    
    for (let i = n - 1; i >= 0; i--) {
        for (let j = m - 1; j >= 0; j--) {
            if(mat[i][j] !== 0) {
                let down = (i < n - 1) ? distances[i + 1][j] : longestDistance;
                let right = (j < m - 1) ? distances[i][j + 1] : longestDistance;
                distances[i][j] = Math.min(Math.min(down, right) + 1, distances[i][j]);
            }
        }
    }
     return distances;
};