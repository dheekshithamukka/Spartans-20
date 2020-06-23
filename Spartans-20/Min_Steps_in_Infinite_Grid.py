class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        dist = 0
        for i in range(len(A)-1):
            dist += max(abs(A[i+1] - A[i]), abs(B[i+1]-B[i]))
        return abs(dist)