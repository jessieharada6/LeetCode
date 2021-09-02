/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
 var canFinish = function(numCourses, prerequisites) {
    let preMap = new Map();
    let visited = new Set(); 
    
    // list every course with corresponding pre (can be empty)
    // 3
    // [[1,0],[2,1]]
    // 0 => [], 1 => [0], 2=> [1]
    for (let i = 0; i < numCourses; i++) {
        preMap.set(i, []);
    }
    for (let [course, pre] of prerequisites) {
        preMap.get(course).push(pre)
    }
    
    
    for (let course = 0; course < numCourses; course++) {
        if (dfs(course) === false)
            return false;
    }
    return true;
    
    function dfs(course) {
        if (visited.has(course)) {
            return false;
        }
        if (preMap.has(course) && preMap.get(course).length === 0) {
            return true;
        }
        
        visited.add(course);
        
        // for ... of (numeric)
        for (const pre of preMap.get(course)) {
            if (dfs(pre) === false)
                return false;
        }
        
        visited.delete(course);
        if (preMap.has(course))
            preMap.get(course).length = 0;
        return true;
    } 
    
};
