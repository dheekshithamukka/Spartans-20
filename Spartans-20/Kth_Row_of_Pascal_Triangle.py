class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        row = [1] * (A+1)

        for i in range(A):
            for k in range(i, 0, -1):
                row[k] = row[k] + row[k-1]
    
        return row