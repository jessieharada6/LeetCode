/**
 * @param {number[][]} isConnected
 * @return {number}
 */
 var findCircleNum = function(isConnected) {
    let n = isConnected.length;
    let output = 0;
    let visited = new Set();
    
    for (let city = 0; city < n; city++) {
        if (!visited.has(city)) {
            output += 1;
            dfs(city);
        }
    }
    
    return output;
    
    function dfs(city) {
        visited.add(city);
        
        for (let sister = 0; sister < n; sister++) {
            if (isConnected[city][sister]
                && !visited.has(sister))
                dfs(sister);
        }
    }
};