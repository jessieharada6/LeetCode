var minDepth = function (root) {
    return dfs(root);
    function dfs(root) {
        if (!root) return 0;
        if (!root.left) return dfs(root.right) + 1;
        if (!root.right) return dfs(root.left) + 1;
        return Math.min(dfs(root.left), dfs(root.right)) + 1;
    }
};
