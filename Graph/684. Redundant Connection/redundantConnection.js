/**
 * @param {number[][]} edges
 * @return {number[]}
 */
 var findRedundantConnection = function(edges) {
    let n = edges.length; 
    let parents = [];
    for (let i = 0; i < n + 1; i++) {
        parents[i] = i;
    }
    let ranks = new Array(n + 1).fill(1);
    
    // console.log(parents, ranks);
    
    for (let [n1, n2] of edges) {
        if (!union(n1, n2)) {
            return [n1, n2];
        }
    }
    
    function find(n) {
        let p = parents[n];
        
        while (p !== parents[p]){
            parents[p] = parents[parents[p]];
            p = parents[p];
        }
        
        return p;
    }
    
    function union(n1, n2) {
        let p1 = find(n1);
        let p2 = find(n2);
        
        if (p1 === p2) {
            return false;
        }
        
        if (ranks[p1] > ranks[p2]) {
            parents[p2] = p1;
            ranks[p1] += ranks[p2]; 
        } else {
            parents[p1] = p2;
            ranks[p2] += ranks[p1];
        }
        
        return true;
    }
};