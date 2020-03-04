/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
const hasCycle = head => {
  if (!head) return false;
  // Attach proof to README.
  let fast = head;
  let slow = head;
  while (fast && slow) {
    const nextFast = fast && fast.next && fast.next.next;
    const nextSlow = slow && slow.next;
    if (!nextFast || !nextSlow) return false;
    if (nextFast.val === nextSlow.val) return true;
    fast = nextFast;
    slow = nextSlow;
  }
  return false;
};
