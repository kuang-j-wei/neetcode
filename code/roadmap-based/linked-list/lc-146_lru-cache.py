class ListNode:
    def __init__(self, val=None, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:
    """
    Since we need to know the history of what key was accessed at what
    point in time, we can think of the history as a Linked List. Then
    the head will always be the oldest node that was accessed, and the
    tail will be the most recent. Then if the cache is full, we can just
    remove the head node and place the new head node as the next node of
    the "old" head node. And whenever we update a node's value, or we
    access a key's value, we will also update the corresponding node to
    the tail. And since we may need to move a node from the middle of
    the linked list to the tail, we can only achieve this in O(1) time
    if we use a doubly linked list. In addition, instead a ListNode only
    storing the value, we also need to store the original key of it so
    that when we are removing a head, we can remove the key from the
    cache as well.

    Time Complexity: O(1)
        We will always only need o update the head and tail, and also
        a node that may be in the middle of the doubly link list, which
        is still an O(1) operation

    Space Complexity: O(k)
        Where the k is the capacity itself
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # we will let this cache to return the node, then we return node.val as the
        self.dummy = ListNode()
        self.tail = self.dummy

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # need to update linked list and return cache
        node = self.cache[key]
        # update it to the tail, if it's not already the tail
        if self.tail != node:
            self.update_node_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update a value, and update the tail
            node = self.cache[key]
            node.val = value
            if self.tail != node:
                self.update_node_to_tail(node)
        elif len(self.cache) >= self.capacity:
            # need to evict then add a new node
            ## fist pop the head key from the cache
            self.cache.pop(self.dummy.next.key)
            ## then if this is not the only node in the list, manipulate
            ## the links to remove this head node
            if self.tail != self.dummy.next:
                # there is more than one node in the linked list
                self.dummy.next = self.dummy.next.next
                self.dummy.next.prev = self.dummy
            ## otherwise, head was the only node, so now we should only
            ## have dummy in the linked list
            else:
                self.dummy.next = None
                self.tail = self.dummy
            ## then add this new node to the tail and to the cache
            node = ListNode(val=value, key=key)
            self.cache[key] = node
            self.add_to_tail(node)
        else:
            # adding a new value and don't need to evict
            node = ListNode(val=value, key=key)
            self.cache[key] = node
            self.add_to_tail(node)

    def update_node_to_tail(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = self.tail.next

    def add_to_tail(self, node):
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)