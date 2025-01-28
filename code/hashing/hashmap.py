class Pair:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.hash_table = [None] * self.capacity

    def _hashing(self, key: int) -> int:
        ascii_sum = 0
        if isinstance(key, str):
            for c in key: 
                ascii_sum += ord(c)
        else:
            ascii_sum = key

        hash = ascii_sum % self.capacity

        return hash

    def get(self, key: int) -> int:
        hash = self._hashing(key)
        result = -1

        if self.hash_table[hash] is not None:
            node = self.hash_table[hash]
            if node.key == key:
                result = node.val
            else:
                while node:
                    if node is not None and node.key == key:
                        result = node.val
                        break
                    elif node is not None:
                        node = node.next
        return result

    def insert(self, key: int, value: int) -> None:
        if (self.len + 1) >= self.capacity // 2:  # +1 is needed to pretend we've gone ahead and inserted already
            self.resize()
        
        hash = self._hashing(key)
        node = self.hash_table[hash]

        if node is None:  # current slot empty
            self.hash_table[hash] = Pair(key, value)
            self.len += 1  # these len + 1 can't be done before hand because in self.resize len gets re-calculated
        elif node.key == key:  # current slot already occupied by the exact key, just modify value in place
            node.val = value
        else:  # collision, either go to the tail end or modifies the middle node with matching key with new value
            while node.next:
                if node.next.key == key:
                    node.next.val = value
                    return None
                else:
                    node = node.next
            node.next = Pair(key, value)
            self.len += 1

    def resize(self) -> None:
        old_table = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        self.len = 0  # later insert will re adjust size

        for node in old_table:
            while node:
                self.insert(node.key, node.val)
                node = node.next  # we need to make sure all collision chains are still inserted back, and this will make sure self.len gets incremented

    def remove(self, key: int) -> bool:
        if self.get(key) == -1:
            return False
        
        hash = self._hashing(key)
        node = self.hash_table[hash]
    
        if node.key == key and node.next is None:
            self.hash_table[hash] = None
            self.len -= 1
            return True

        while node.next is not None:
            if node.next.key == key:
                node.next = node.next.next
                self.len -= 1
                break
            else:
                node = node.next
        return True


    def getSize(self) -> int:
        return self.len
    
    def getCapacity(self) -> int:
        return self.capacity