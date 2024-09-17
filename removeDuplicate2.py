# Remove Duplicates from Unsorted Linked List
# Problem: Given the head of an unsorted linked list, remove all duplicates such that each element appears only once. You may not sort the list.

# Example:
# Input: head = [4, 5, 4, 3, 2, 5, 1]
# Output: [4, 5, 3, 2, 1]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class removeDuplicates:
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

    def clean(self):
        prev = None
        temp = self.head
        list = set()
        while temp.next:
            if temp.data not in list:
                list.add(temp.data)
                prev = temp
                temp = temp.next
            else:
                prev.next = temp.next
                temp = temp.next

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end='->' if temp.next else '')
            temp = temp.next


rem = removeDuplicates()
rem.add(4)
rem.add(5)
rem.add(4)
rem.add(3)
rem.add(2)
rem.add(5)
rem.add(1)

rem.print()
print()
print('After cleaning:')
rem.clean()

rem.print()
