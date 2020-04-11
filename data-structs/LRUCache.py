class Node:
    def __init__(self, k: int, v: int, prev: 'Node' = None, next: 'Node' = None) -> None:
        self.key = k
        self.val = v
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity # Assume positive
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lookup = {}
        # Pop things close to head

    def get(self, key: int) -> int:
        if key in self.lookup:
            n = self.lookup[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])
        n = Node(key, value)
        self.add(n)
        self.lookup[key] = n
        if len(self.lookup) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.lookup[n.key]

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
