/**
 * @param {string} expression
 * @return {number[]}
 */
 var diffWaysToCompute = function(expression) {
    let result = []
    
    for (let i = 0; i < expression.length; i++) {
        // it is a sign at index of i
        if (isNaN(expression[i])){
            // [i] is the index for the sign
            let left = diffWaysToCompute(expression.substring(0, i))
            let right = diffWaysToCompute(expression.substring(i + 1))

            for (let l of left) {
                for (let r of right) {
                    l = Number(l)
                    r = Number(r)
                    
                    if (expression[i] === "+") {
                        result.push(l + r)
                    } 
                    else if (expression[i] === "-") {
                        result.push(l - r)
                    } else if (expression[i] === "*") {
                        result.push(l * r)
                    }
                }
            }
        }
    }
    
    if (result.length !== 0) 
        return result
    // no operator
    return [expression]
    
};