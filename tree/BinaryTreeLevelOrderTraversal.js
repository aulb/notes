/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
const levelOrder = root => {
  if (!root) return [];
  const createNodeWithLevel = (node, level) => ({node, level});
  const toVisit = [createNodeWithLevel(root, 0)];
  const levels = [];

  while (toVisit.length) {
    const { node, level } = toVisit.pop();
    if (!levels[level]) levels[level] = [];
    levels[level].push(node.val);

    if (node.right) toVisit.push(createNodeWithLevel(node.right, level + 1));
    if (node.left) toVisit.push(createNodeWithLevel(node.left, level + 1));
  }

  return levels;
};
