test = int(input())
for t in range(test):
	m, n = map(int, input().split(' '))
	m = int(str(m)[::-1])
	n = int(str(n)[::-1])
	ans = 0
	result = 0
	ans = m + n
	result = int(str(ans)[::-1])
	print(result)