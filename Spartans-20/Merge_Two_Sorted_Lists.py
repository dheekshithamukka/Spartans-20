class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        dummy = ListNode(0)
        current = dummy
        while True:
            if not A:
                current.next = B
                break
            if not B:
                current.next = A
                break
            if A.val <= B.val:
                current.next = A
                A = A.next
            else: 
                current.next = B
                B = B.next
            current = current.next
        return dummy.next
