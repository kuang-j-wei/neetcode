# This is essentially LC 707 - Design Linked List

class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index):
        if index > self.size - 1:
            return -1
        elif index == 0:
            return self.head.val
        elif index == self.size - 1:
            return self.tail.val
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr.val
        
    def addAtHead(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def addAtTail(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        if index > self.size:
            return None
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            curr = self.head
            for _ in range(index):
                curr = curr.next
            new_node.prev = curr.prev
            curr.prev.next = new_node
            new_node.next = curr
            curr.prev = new_node
            self.size += 1
    
    def deleteAtIndex(self, index):
        if index > self.size - 1:
            return None

        if self.size == 1:
           self.head = None
           self.tail = None
        elif self.size == 2 and index == 0:
            self.tail.prev = None
            self.head = self.tail
        elif self.size == 2 and index == 1:
            self.head.next = None
            self.tail = self.head
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            
            prev = curr.prev
            nxt = curr.next
            if index == 0:
                nxt.prev = prev
                self.head = nxt
            elif index == self.size - 1:
                prev.next = nxt
                self.tail = prev
            else:
                prev.next = nxt
                nxt.prev = prev
        self.size -= 1
            
    def removeAtTail(self):
        if self.size == 0:
            return None

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            tmp_prev = self.tail.prev
            tmp_prev.next = None
            self.tail.prev = None
            self.tail = tmp_prev
        self.size -= 1
