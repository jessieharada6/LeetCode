var pathSum = function (root, targetSum) {
    let paths = [];
    dfs(root, targetSum, [], paths);
    return paths;

    function dfs(root, targetSum, path, paths) {
        if (!root) return 0;
        targetSum -= root.val;
        path.push(root.val);

        if (targetSum === 0 && !root.left && !root.right) {
            paths.push([...path]);
            return;
        }

        dfs(root.left, targetSum, [...path], paths);
        dfs(root.right, targetSum, [...path], paths);
    }
};