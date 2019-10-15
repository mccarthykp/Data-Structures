# SINGLY LINKED LIST W/ countNodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next

def countNodes(head):
    num_nodes = 1
    current = head
    while current.next != None:
        num_nodes += 1
        current = current.next
    return num_nodes

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

print(countNodes(nodeA))