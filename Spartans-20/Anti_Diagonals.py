class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        
        b = [[] for i in range(2*len(A)-1)]
        
        for i in range(len(A)):
            for j in range (len(A)):
                sum = i + j
                b[sum].append(A[i][j])
        return b