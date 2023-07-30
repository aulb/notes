class Node:
    def __init__(self, key: int, value: int, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"${self.key}:{self.value}"

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.sentinel = Node(0, 0)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def _add(self, node: Node) -> None:
        # Always add from behind (for now)
        prev = self.sentinel.prev 
        prev.next, self.sentinel.prev = node, node
        node.next, node.prev = self.sentinel, prev
        self.lookup[node.key] = node

    def _remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del self.lookup[node.key]

    def get(self, key: int) -> int:
        if key not in self.lookup: return -1
        node = self.lookup[key]
        self._remove(node)
        self._add(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.value = value
            self._remove(node)
            self._add(node)
            return
        if len(self.lookup) == self.capacity:
            self._remove(self.sentinel.next)
        node = Node(key, value)
        self._add(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#### Old below



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

### Sol 2
class Node:
    def __init__(self, key: int, value: int, prevNode: 'Node' = None, nextNode: 'Node' = None):
        self.key = key
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.nextNode = self.tail
        self.tail.prevNode = self.head
        self.storage = {}
        # self.length = 0 # No need for self.length can do len(self.storage)

    def get(self, key: int) -> int:
        if key not in self.storage: return -1
        # remove from chain add from the back
        node = self.storage[key]
        self.remove(node)
        self.add(node)
        return node.value
        
    def remove(self, node: Node) -> None:
        # Remove from chain
        prevNode = node.prevNode
        nextNode = node.nextNode
        prevNode.nextNode = nextNode
        nextNode.prevNode = prevNode
        del self.storage[node.key] # Book keeping 

    def add(self, node: Node) -> None:
        # Adding from behind
        tailPrevNode = self.tail.prevNode
        tailPrevNode.nextNode = node
        self.tail.prevNode = node
        # Link node together
        node.nextNode = self.tail
        node.prevNode = tailPrevNode
        self.storage[node.key] = node

    def put(self, key: int, value: int) -> None:
        # If key already there, delete and replace
        if key in self.storage:
            self.remove(self.storage[key])
        if len(self.storage) == self.capacity:
            self.remove(self.head.nextNode)
        self.add(Node(key, value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
