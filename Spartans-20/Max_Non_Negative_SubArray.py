class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        m = []
        temp = []
        i = 0
        
        while i < len(A):
            if A[i] >= 0:
                temp.append(A[i])

                if sum(m) == sum(temp):
                    if len(m) < len(temp):
                        m = temp
                elif sum(m) < sum(temp):
                        m = temp
            else:
                temp = []
            i += 1
        return m
