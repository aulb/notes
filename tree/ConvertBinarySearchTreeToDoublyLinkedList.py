class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val) + ' left: ' + self.left.repr() + ' right: ' + self.right.repr()

class LLNode:
    def __init__(self, val: int, prev: 'LLNode' = None, next: 'LLNode' = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    # def __repr__(self):
    #     nextStr = 'next:' + self.next.__repr__() if self.next else 'next: None '
    #     prevStr = 'prev:' + self.prev.__repr__() if self.prev else 'next: None'
    #     return str(self.val) + nextStr + prevStr

# BST -> Doubly LL
#     2
# 1       4
#       3    5
# b <-> a <-> d <-> c <-> e
# 0 <-> 1 <-> 2 <-> 3 <-> 4
# Left Current Right
def convertBSTToDLL(root: 'TreeNode') -> 'LLNode':
    head = prev = LLNode(0)
    def traverse(node: 'TreeNode') -> None:
        global prev
        if not node: return None
        traverse(node.left)
        curr = LLNode(node.val)
        curr.prev = prev
        prev.next = curr
        prev = curr
        traverse(node.right)
    traverse(root)
    return head.next

bst = TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5)))
print(convertBSTToDLL(bst))
