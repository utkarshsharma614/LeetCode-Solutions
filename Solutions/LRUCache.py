class dll:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head = dll(-1, -1)
        self.tail = self.head
        self.hash = {}
        self.capacity = capacity
        self.length = 0
        

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        
        node = self.hash[key]
        val = node.val
        
        if node.next:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        
        return val
            
    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            
            if node.next:
                node.next.prev = node.prev
                node.prev.next = node.next
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        
        else:
            node = dll(key, value)
            self.hash[key] = node
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            self.length += 1
            
            if self.length > self.capacity:
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.hash[remove.key]
                self.length -= 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)