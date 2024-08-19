class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head
        while current:
            print(current.data, end='->' if current.next else '\n')
            current = current.next


ll = LinkedList()
ll.add(5)
ll.add(10)
ll.add(15)
ll.add(2)
ll.add(6)

ll.printLL()
