/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */
/**
 * @param {Node} node
 * @return {Node}
 */

// DFS
 var cloneGraph = function(node, map = new Map()) {
    if (!node) return null;
    
    // O(n) as map is to memorise the visited node
    if (map.has(node)) 
        return map.get(node);
    
    // cloned node
    let copy = new Node(node.val);
    // map is to record the visited node
    map.set(node, copy);
    // traverse node's neighbors
    for (let n of node.neighbors) {
        copy.neighbors.push(cloneGraph(n, map));
    }
    
    return copy;
};


 // BFS
 var cloneGraph = function(node, map = new Map()) {
    if (!node) return null;
    
    map.set(node, new Node(node.val));
    let queue = [node];
    
    while (queue.length) {
        let current = queue.shift();
        for (let n of current.neighbors) {
            if (!map.has(n)) {
                map.set(n, new Node(n.val));
                queue.push(n);
            } 
            //undirected so both edges need to be connected
            map.get(n).neighbors.push(map.get(current));
        }
    }
    
    return map.get(node);
};

