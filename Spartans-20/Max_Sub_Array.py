class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, a):
        max_sum = a[0]
        curr_max = a[0]
        for i in range(1,len(a)):
            curr_max = max(a[i], curr_max+a[i])
            max_sum = max(max_sum, curr_max)
        return max_sum
