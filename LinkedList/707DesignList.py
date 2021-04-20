#Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
#A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
#If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
#


class Node:
    def __init__(self,x):

        self.next = None
        self.prev = None
        self.val = x

class MyLinkedList:

    def __init__(self):

        self.head = Node(0)
        self.len = 0

        """
        Initialize your data structure here.
        """

    def get(self, index: int) -> int:

        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.len:
            return -1

        curr = self.head

        for _ in range(index + 1):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node           will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.len, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if self.len < index:
            return

        if index < 0:
            index = 0

        self.len += 1
        pred = self.head

        for _ in range(index):
            pred = pred.next

        new = Node(val)
        new.next = pred.next
        pred.next = new


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.len:
            return

        self.len -= 1
        pred = self.head

        for _ in range(index):
            pred = pred.next

        pred.next = pred.next.next
