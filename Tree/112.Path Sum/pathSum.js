var hasPathSum = function (root, targetSum) {
    let result = false;
    dfs(root, targetSum);
    return result;

    function dfs(root, targetSum) {
        if (!root) return false;

        targetSum -= root.val;
        if (targetSum === 0 && !root.left && !root.right) {
            result = true;
        }

        dfs(root.left, targetSum);
        dfs(root.right, targetSum);
    }
};