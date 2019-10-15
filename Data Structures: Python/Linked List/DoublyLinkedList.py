# DOUBLY LINKED LIST 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def traverse(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next

nodeA = Node(6)
nodeB = Node(4)
nodeC = Node(2)
nodeD = Node(1)
nodeE = Node(7)
nodeF = Node(3)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF

nodeB.prev = nodeA
nodeC.prev = nodeB
nodeD.prev = nodeC
nodeE.prev = nodeD

print(nodeB.prev.data)