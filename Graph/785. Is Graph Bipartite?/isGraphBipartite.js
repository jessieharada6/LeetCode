/**
 * @param {number[][]} graph
 * @return {boolean}
 */
 var isBipartite = function(graph) {
    // 1 <= n <= 100
    let visited = new Array(100).fill(false);
    let colors = new Array(100).fill(false);
    let queue = [];
    
    for (let i = 0; i < graph.length; i++) {
        // only visit what has not been visited
        if (graph[i].length === 0 || visited[i] === true) {
            continue;
        }
        
        // queue contains what'll be visited
        queue.push(i);
        visited[i] = true;
        colors[i] = true;
        
        while (queue.length !== 0) {
            let node = queue.pop();
            
            for (let neighbour of graph[node]) {
                if (visited[neighbour] === false){
                    queue.push(neighbour);
                    visited[neighbour] = true;
                    // toggle colors
                    colors[neighbour] = !colors[node];  
                }
                else if (colors[node] === colors[neighbour]) {
                    return false;
                }
            } 
        }
    }
    
    return true;
};