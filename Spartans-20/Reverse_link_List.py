class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, A, B, C):
	    if A==None:
            return None
        head = A
        first_join = None
        if B>1:
            first_join = A
            temp_B = B
            while temp_B>2:
                temp_B -= 1
                first_join = first_join.next
        while B>1:
            B -= 1
            C -= 1
            A = A.next
        second_join = A
        prev = None
        while C>0:
            C -= 1
            temp = A.next
            A.next = prev
            prev = A
            A = temp
        second_join.next = A
        if first_join is None:
            return prev
        first_join.next = prev
        return head


