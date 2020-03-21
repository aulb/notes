/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const mergeTwoLists = (l1, l2) => {
  let head = null;
  let curr = null;

  // While l1 or l2 is not null
  while (l1 || l2) {
    const l1v = l1 && typeof l1.val === 'number' ? l1.val : Infinity;
    const l2v = l2 && typeof l2.val === 'number' ? l2.val : Infinity;
    const newListNode = new ListNode();
    if (l1v < l2v && l2v !== Infinity) {
      newListNode.val = l1v;
      l1 = l1.next;
    }

    if (l1v >= l2v && l1v !== Infinity) {
      newListNode.val = l2v;
      l2 = l2.next;
    }

    if (!head) {
      head = newListNode;
      curr = head;
    } else {
      head.next = newListNode;
      curr = head.next;
    }
  }

  return head;
};
