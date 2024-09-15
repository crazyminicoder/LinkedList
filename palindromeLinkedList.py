class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class palindrome:
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

    def reverse(self):
        if self.head is None:
            print('The list is empty')
            return

        stack = []

        temp = self.head
        while temp:
            stack.append(temp.data)
            temp = temp.next

        print('stack: ', stack)

        if stack == stack[::-1]:
            print('The list is a palindrome')
        else:
            print('The list is not a palindrome')


pal = palindrome()

pal.add(1)
pal.add(2)
pal.add(2)
pal.add(1)

pal.reverse()
