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