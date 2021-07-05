/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
    let result = [];
    let stack = [];
    backtrack(0, 0);
    return result;

    function backtrack(openC, closedC) {
        if (openC === n && closedC === n) {
            result.push(stack.join(""));
            return;
        }

        if (openC < n) {
            stack.push("(");
            // 1. openC++: maximum stack 
            //    stack.push("("); RangeError: Maximum call stack size exceeded
            // 2. openC += 1: add to 1 immediantly, will not start from 0
            backtrack(openC + 1, closedC);
            // global var, we won't carry
            stack.pop();
        }

        if (closedC < openC) {
            stack.push(")");
            backtrack(openC, closedC + 1);
            stack.pop();
        }
    }
};