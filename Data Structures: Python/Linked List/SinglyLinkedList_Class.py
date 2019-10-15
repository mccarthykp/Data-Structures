# SINGLY LINKED LIST CLASS
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'

    def prepend(self, data):
        self.head = Node(data=data, next=self.head)
    
    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(data=data)

    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr
        
    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next 
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node