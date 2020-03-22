/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
const removeNthFromEnd = (head, n) => {
  if (!head) return head;
  // Two pass
  // n = 2 from behind means true n = k - n from front
  let headCopy = head;
  let length = 0;
  while (headCopy) {
    length++;
    headCopy = headCopy.next;
  }
  const toRemove = length - n;
  if (!toRemove) return head.next;

  let curr = head;
  let prev = null;
  let counter = 0;
  while (counter !== toRemove) {
    prev = curr;
    curr = curr.next;
    counter++;
  }

  prev.next = curr.next;
  return head;
};

// One pass, there isn't a one pass algo. Two pointers but advancing n spaces apart.
