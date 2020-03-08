/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} s
 * @param {TreeNode} t
 * @return {boolean}
 */
const isSubtree = (s, t) => {
  // Worst case is O(n^2), because we need to check:
  // n + n - 1 + n - 2 ... => n^2
  // s, t non empty
  if (!s) return false;
  if (isSameTree(s, t)) return true;
  return isSubtree(s.left, t) || isSubtree(s.right, t);
};

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
const isSameTree = (p, q) => {
  // if (!p && !q) return true;
  // else if (!p && q) return false;
  // else if (p && !q) return false;
  // else if (p.val !== q.val) return false;
  // return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
  if (!p && !q) return true;
  else if (p && q) return p.val === q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
  return false;
};
