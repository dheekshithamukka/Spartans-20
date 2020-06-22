class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n=len(A)
        seen=[False]*n
        for el in A:
            if seen[el]==True:
                return el
            else:
                seen[el]=True
        return -1
            