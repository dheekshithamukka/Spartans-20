class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        for i in range(0, len(A)):
            if A[i] == B:
                return i
            if A[0] < B and A[i] < A[0]: # Based on the graph, we can stop here
                return -1
        return -1