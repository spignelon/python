class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

family.traversal()
