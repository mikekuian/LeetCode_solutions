#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        def mergeTwoLists(list1, list2):

            head = ListNode()

            p = head

            while list1 and list2:

                if list1 and list2 and list1.val <= list2.val:
                    p.next = list1
                    list1 = list1.next

                elif list1 and list2 and list2.val <= list1.val:
                    p.next = list2
                    list2 = list2.next

                p = p.next

            if list1:
                while list1:
                    p.next = list1
                    list1 = list1.next
                    p = p.next
            if list2:
                while list2:
                    p.next = list2
                    list2 = list2.next
                    p = p.next

            return head.next

        buf = []

        for l in lists:
            buf = mergeTwoLists(buf, l)

        return buf
