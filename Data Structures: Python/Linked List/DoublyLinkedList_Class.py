# DOUBLY LINKED LIST CLASS
class Node:
    def __init__(self, data=None, next=None, prev=None):
        # creates node element with attributes data, prev, next
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        # returns string representation of the node
        return repr(self.data)

class DoublyLinkedList:
    def __init__(self):
        # creates empty linked list
        self.head = None

    def prepend(self, data):
        # adds element to beginning of linked list
        new_node = Node(data=data, next=self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        
    def append(self, data):
        # add element to end of linked list
        # edge cases: empty list
        new_node = Node(data=data)
        curr = self.head
        if curr == None:
            self.head = new_node
            return
        while curr != None:
            curr = curr.next
        if curr.next == None:
            new_node = curr.next
        
    def find(self, key):
        # returns first element with data matching key, if key not found returns None
        curr = self.head
        if self.head.data == key:
            return self.head
        while curr.data != key:
            curr = curr.next
        if curr.data == key:
            return curr

    def remove_element(self, node):
        # removes element from linked list
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.next = None
        node.prev = None
        
    def remove(self, key):
        # removes first element with matching key
        pass

    def reverse(self):
        # reverses linked list in place
        pass