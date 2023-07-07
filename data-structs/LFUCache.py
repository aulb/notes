# 1034
from collections import defaultdict
class Node:
    def __init__(self, key: int, value: int, freq: int):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.sentinel = Node(0, 0, 0)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, node: Node) -> None:
        node.next = self.sentinel.next
        node.prev = self.sentinel
        node.next.prev = node
        self.sentinel.next = node
        self.size += 1

    def pop(self, node: Node = None) -> Node: # Popping node good trick
        if self.size == 0: return
        if node is None:
            node = self.sentinel.prev
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1
        return node

    # def getTail(self) -> Optional[Node]: # Pretty much pop without any param right??
    #     if self.size == 0: return None
    #     return self.sentinel.prev

class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.nodes = {}
        self.freqs = defaultdict(DoublyLinkedList)
        self.minFreq = 0

    def _update(self, node: Node) -> None:
        freq = node.freq
        self.freqs[freq].pop(node)
        if self.minFreq == freq and not self.freqs[freq]: # not dll => True if len(dll) is 0
            self.minFreq += 1
        node.freq += 1
        self.freqs[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.nodes: return -1
        node = self.nodes[key]
        self._update(node)
        return node.value 

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self._update(node)
            node.value = value
            return
        
        if self.size == self.capacity:
            node = self.freqs[self.minFreq].pop()
            del self.nodes[node.key]
            self.size -= 1
        
        node = Node(key, value, 1)
        self.nodes[key] = node
        self.freqs[1].append(node)
        self.minFreq = 1            
        self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    dll = DoublyLinkedList()
    print(len(dll))
    print(not dll)