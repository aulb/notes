/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
const maxDepth = root => {
  let maxDepth = 0;
  if (!root) return maxDepth;

  // DFS or BFS is equally fine, practice DFS without recursion
  const makeNodeWithDepth = (node, depth) => ({ node, depth });
  const toVisit = [makeNodeWithDepth(root, 1)];
  // const visited = {}; // In BT, I don't need a visited since its going to be one by one
  // Its not a connected graph

  while (toVisit.length) {
    const { node, depth } = toVisit.pop();
    if (depth > maxDepth) maxDepth = depth;
    if (node.left) toVisit.push(makeNodeWithDepth(node.left, depth + 1));
    if (node.right) toVisit.push(makeNodeWithDepth(node.right, depth + 1));
  }

  return maxDepth;
};
