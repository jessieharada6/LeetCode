/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
 var findMinHeightTrees = function(n, edges) {
    //edge case
    if (n === 1) return [0];
    
    let output = [];
    
    // set up map to present graph
    // set up degree for each node
    let map = new Map();
    let degree = new Array(n).fill(0);
    
    for (let i = 0; i < n; i++) {
        map.set(i, []);
    }
    for (let [a, b] of edges) {
        map.get(a).push(b);
        map.get(b).push(a);
        degree[a]++;
        degree[b]++;
    }
    
    // console.log(map, degree)
    
    // record the node with least edges
    let queue = [];
    for (let i = 0; i < degree.length; i++) {
        if (degree[i] === 1) 
            queue.push(i)
    }
    
    console.log(queue)
    while (queue.length) {
        // temp list to save the final results
        let list = [];
        let size = queue.length;
        for (let i = 0; i < size; i++) {
            let current = queue.shift();
            list.push(current);
            // console.log(list, queue)
            for (let n of map.get(current)) {
                degree[n]--;
                if (degree[n] === 1) queue.push(n);
            }
        }
        output = list;
    }
    
    return output;
};