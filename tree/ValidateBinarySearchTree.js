/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 * RECURSIVE, its NOT enough to get the min/max value from one above
 * We need the min max boundary everytime, don't forget to not use the tertiary operator
 * min = 0
 * Mistake 1: 0 ? condition A : true;
 */
const isNodeValueInBetween = (root, min, max) => {
  if (!root) return true;
  const { left, right, val } = root;
  const isMoreThanMin = typeof min === 'number' ? val > min : true;
  const isLessThanMax = typeof max === 'number' ? max > val : true;
  return isMoreThanMin && isLessThanMax && isNodeValueInBetween(left, min, val) && isNodeValueInBetween(right, val, max);
};

const isValidBST = root => {
  if (!root) return true;
  return isNodeValueInBetween(root, null, null);
};
