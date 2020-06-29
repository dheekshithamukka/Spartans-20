class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
	    if(A<B):
	        A, B = B, A
	    while(B):
	        A, B = B, A%B
	    return A