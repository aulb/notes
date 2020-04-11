# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## O(nlogn) runtime
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return
        # Single node left
        if not head.next: return TreeNode(head.val)
        #[1,2,3,4,5] => 3 is middle
        #[1,2,3,4,5,6] => 3 is middle
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next # 4,5,6->None
        slow.next = None # 1,2,3->None
        root = TreeNode(tmp.val) # 4
        root.left = self.sortedListToBST(head) # 1,2,3
        root.right = self.sortedListToBST(tmp.next) # 5 ,6
        return root
