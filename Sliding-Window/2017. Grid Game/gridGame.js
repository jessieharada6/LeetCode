/**
 * @param {number[][]} grid
 * @return {number}
 */
 var gridGame = function(grid) {
    let one = grid[0].reduce((a, b) => a + b) - grid[0][0];
    let two = 0;
    let output = one;
    
    // start from 1, as grid[0][0] is always used by robot 1
    for (let i = 1; i < grid[0].length; i++) {
        one -= grid[0][i];
        // robot1 will go down when switching rows
        // it will occupy the whole columns
        two += grid[1][i - 1]
        
        output = Math.min(output, Math.max(one, two));
    }
    
    return output;
};