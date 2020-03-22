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
  const dummy = new ListNode();
  let curr = dummy;

  while (l1 && l2) {
    if (l1.val > l2.val) {
      curr.next = l2;
      l2 = l2.next;
    } else {
      curr.next = l1;
      l1 = l1.next;
    }
    curr = curr.next;
  }
  // Will always be imbalanced
  curr.next = l1 || l2;
  return dummy.next;
};

const getVal = node => node && typeof node.val === 'number' ? node.val : Infinity;
/*
1        1    - same size
1        null - l1 is greater
null     1    - l2 is greater
*/
const mergeTwoListsMyWay = (l1, l2) => {
  let head = null;
  let curr = null;
  while (l1 || l2) { // null || null, escape
    const l1v = getVal(l1); // inf
    const l2v = getVal(l2); // 1
    const newNode = new ListNode();
    if (l2v >= l1v && l1v !== Infinity) {
      newNode.val = l1v;
      l1 = l1.next; // null
    } else if (l1v > l2v && l2v !== Infinity) {
      newNode.val = l2v;
      l2 = l2.next;
    }

    if (!head) { // new node is head, // curr is head
      head = newNode;
      curr = head;
    } else {
      curr.next = newNode; // 1->newNode
      curr = curr.next; // curr new node
    }
  }

  return head;
};
