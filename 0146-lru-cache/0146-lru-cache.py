class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = collections.defaultdict(Node)
        self.lru = Node(-1, -1)
        self.mru = Node(-1, -1)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def remove(self, node):
        val = node.val
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        return val
    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        node.prev, prev.next = prev, node
        node.next, nxt.prev = nxt, node
    def get(self, key: int) -> int:
        if key in self.keyToNode:
            # remove the node
            val = self.remove(self.keyToNode[key])
            # replace the node
            self.insert(self.keyToNode[key])
            # return the node's val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            # remove the node
            _ = self.remove(self.keyToNode[key])
        # insert the node
        self.keyToNode[key] = Node(key, value)
        self.insert(self.keyToNode[key])
        if self.capacity < len(self.keyToNode):
            # remove lru, delete its reference in keyToNode
            lru_node = self.lru.next
            lru_node_next = lru_node.next
            # move lru to new node
            self.lru.next = lru_node.next
            lru_node_next.prev = self.lru

            del self.keyToNode[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)