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
        self.len += 1

        if self.len >= self.capacity // 2:
            self.resize()
        
        hash = self._hashing(key)
        node = self.hash_table[hash]

        if node is None:
            self.hash_table[hash] = Pair(key, value)
        elif node.key == key:
            node.val = value
        else:  # collision, need to go the the tail end, but we also might have to update middle
            while node.next:
                if node.next.key == key:
                    node.next.val = value
                    return None
                else:
                    node = node.next
            node.next = Pair(key, value)

    def resize(self) -> None:
        old_table = self.hash_table
        self.capacity *= 2
        self.hash_table = [None] * self.capacity
        self.len = 0  # later insert will re adjust size

        for node in old_table:
            if node:
                self.insert(node.key, node.val)

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