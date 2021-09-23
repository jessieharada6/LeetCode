/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
 var calcEquation = function(equations, values, queries) {
    let graph = new Map();
    let result = []
    
    // build graph
    for (let i = 0; i < equations.length; i++) {
        let x = equations[i][0];
        let y = equations[i][1];
        
        if (!graph.has(x)) {
            graph.set(x, new Map());
        }
        graph.get(x).set(y, values[i]);
        
        if (!graph.has(y)) {
            graph.set(y, new Map());
        }
        graph.get(y).set(x, 1/values[i])
    }
    
    // bfs
    for (let [src, dst] of queries) {
        result.push(bfs(src, dst));
    }
    
    return result;
    
    function bfs(src, dst) {
        if (!graph.has(src) || !graph.has(dst)) 
            return -1.0;
        
        let queue = [[src, 1.0]];
        let visited = new Set();
        
        for (let [x, val] of queue) {
            if (x === dst)
                return val;
            visited.add(x);
            
            for (let [y, v] of graph.get(x)) {
                if (!visited.has(y)) {
                    // needs to use the updated val in queue
                    queue.push([y, val * graph.get(x).get(y)])
                }
            }
        }
        
        return -1.0;
    }

};


//dfs
/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
 var calcEquation = function(equations, values, queries) {
    let result = [];
    let graph = new Map();
    
    for (let i = 0; i < equations.length; i++) {
        let x = equations[i][0];
        let y = equations[i][1];
        
        if (!graph.has(x)) {
            graph.set(x, new Map());
        }
        graph.get(x).set(y, values[i]);
        
        if (!graph.has(y)) {
            graph.set(y, new Map());
        }
        graph.get(y).set(x, 1/values[i]);
    }
    
    for (let [x, y] of queries) {
        let seen = new Set();
        result.push(dfs(x, y, seen));
    }
    
    return result
    
    function dfs(src, dst, seen) {
        if (!graph.has(src) || !graph.has(dst)) {
            return -1.0;
        }
        
        for (let [y, v] of graph.get(src)) {
            if (y === dst) {
                // assign back to weight
                return graph.get(src).get(dst)
            }
        }
        
        seen.add(src);
        
        for (let [y, v] of graph.get(src)) {
            if (!seen.has(y)) {
                let weight = dfs(y, dst, seen);
                if (weight !== -1.0) {
                    return graph.get(src).get(y) * weight;
                }
            }
        }
        
        seen.delete(src);
        return -1.0;
    }
};