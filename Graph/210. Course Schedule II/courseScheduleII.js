/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
 var findOrder = function(numCourses, prerequisites) {
    let preMap = new Map();
    let visited = new Set();
    let cycle = new Set();
    let output = []
    
    for (let i = 0; i < numCourses; i++) {
        preMap.set(i, []);
    }
    for (let [course, pre] of prerequisites) {
        preMap.get(course).push(pre);
    }
    
    for (let i = 0; i < numCourses; i++) {
        if (dfs(i) === false) {
            return [];
        }
    }
    return output;
    
    function dfs(course) {
        if (cycle.has(course)) {
            return false;
        }
        if (visited.has(course)) {
            return true
        }
        
        cycle.add(course);
        for (let pre of preMap.get(course)) {
            if (dfs(pre) === false)
                return false;
        }
        
        cycle.delete(course);
        visited.add(course);
        output.push(course);
        return true; 
    }
};