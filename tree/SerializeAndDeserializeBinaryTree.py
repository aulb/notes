# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def encode(node):
            if node:
                vals.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                vals.append('#')
        vals = []
        encode(root)
        return ' '.join(vals)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # Instead of keeping track of position in array with an index, use an iterator
        def decode():
            val = next(vals)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left = decode()
            node.right = decode()
            return node
        vals = iter(data.split())
        return decode()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
