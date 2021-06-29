var pathSum = function (root, targetSum) {
    if (!root) return 0;

    // console.log(root.val);
    return dfs(root, targetSum)
        + pathSum(root.left, targetSum)
        + pathSum(root.right, targetSum);

    function dfs(root, targetSum) {
        if (!root) return 0;

        // console.log(targetSum, root.val)
        return (targetSum === root.val ? 1 : 0)
            + dfs(root.left, targetSum - root.val)
            + dfs(root.right, targetSum - root.val);
    }
};