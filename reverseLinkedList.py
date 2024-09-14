class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class reverseList:
    def __init__(self):
        self.head = None
        self.head2 = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newNode

    def addNewList(self, data):
        if self.head2 is None:
            self.head2 = Node(data)
            return

        newNode = Node(data)
        temp = self.head2
        while temp.next:
            temp = temp.next

        temp.next = newNode

    def printList(self):
        temp = self.head2
        while temp:
            print(temp.data, end='->' if temp.next else '')
            temp = temp.next

    def reverseKGroup(self, k):
        if self.head is None:
            print('the list is empty')
            return
        count = 0
        stack = []
        temp = self.head
        while temp:
            stack.append(temp.data)
            count += 1
            if count == k:
                while stack:
                    data = stack.pop()
                    self.addNewList(data)
                count = 0
            temp = temp.next
        while stack:
            # Preserve original order for leftover elements
            data = stack.pop(0)
            self.addNewList(data)


rl = reverseList()
rl.add(1)
rl.add(2)
rl.add(3)
rl.add(4)
rl.add(5)
rl.add(6)
rl.add(7)
rl.add(8)

rl.reverseKGroup(3)

rl.printList()
