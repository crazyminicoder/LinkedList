# Problem: Given the head of a singly linked list, return true if it is a palindrome, otherwise return false.

# Example:

# Input: head = [1, 2, 2, 1]
# Output: true

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

        if stack == stack[::-1]:
            return True
        else:
            return False


pal = palindrome()

pal.add(1)
pal.add(2)
pal.add(2)
pal.add(1)

print(pal.reverse())
