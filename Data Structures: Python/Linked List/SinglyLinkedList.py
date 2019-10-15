# SINGLY LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next

nodeA = Node(6)
nodeB = Node(4)
nodeC = Node(2)
nodeD = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD

nodeA.traverse()