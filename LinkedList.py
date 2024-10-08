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

    def removeLast(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        prev = temp
        while temp.next:
            prev = temp
            temp = temp.next

        print("Popped Node:", temp.data)
        temp = None
        prev.next = None

    def search(self, key):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            if temp.data == key:
                print("Key found:", temp.data)
                return
            temp = temp.next
        print("Key not found in the list")

    def reverse(self):
        if self.head is None:
            print("List is empty")
            return
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def insertAtBegning(self, data):
        if self.head is None:
            print("the list is empty")
            return

        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def insertInBetween(self, position, data):
        if self.head is None:
            print("The list is empty")
            return

        if position == 1:
            self.insertAtBegning(data)

        else:
            count = 1
            temp = self.head
            while count < position:
                temp = temp.next
                count += 1

            next = temp.next
            newNode = Node(data)
            temp.next = newNode
            newNode.next = next

    def removeTop(self):
        if self.head is None:
            print('The list is empty')
            return

        temp = self.head
        print("The removed node at top is: ", temp.data)
        self.head = None
        self.head = temp.next

    def removeInBetween(self, key):
        if self.head is None:
            print("The list is empty")
            return
        temp = self.head
        prev = None
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp.data == key:
            next = temp.next
            prev.next = next
        else:
            print("Key not found")


ll = LinkedList()
ll.add(5)
ll.add(10)
ll.add(15)
ll.add(2)
ll.add(6)

ll.printLL()

ll.removeLast()

ll.printLL()

ll.search(5)

ll.reverse()

ll.printLL()

ll.insertAtBegning(33)

ll.printLL()

ll.insertInBetween(3, 7)

ll.printLL()

ll.removeLast()

ll.removeTop()

ll.printLL()

ll.removeInBetween(15)

ll.printLL()
