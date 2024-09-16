# Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = newNode

    def removeDuplicate(self):
        if self.head is None:
            print('The list is empty')
            return
        temp = self.head

        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next

            else:
                temp = temp.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end='->' if temp.next else '')
            temp = temp.next


ll = List()
ll.add(1)
ll.add(1)
ll.add(2)
ll.add(4)
ll.add(1)
ll.add(2)
ll.add(2)
ll.add(2)
ll.add(3)

ll.printList()
print()
print('After removing duplicates:')

ll.removeDuplicate()

ll.printList()
