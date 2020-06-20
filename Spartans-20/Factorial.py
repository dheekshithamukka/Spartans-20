def fact(n):
    zeroes = 0
    while n >= 5:
        n //= 5
        zeroes += n
    return zeroes
t=int(input())
while t>0:
    n=int(input())
    print(fact(n))
    t=t-1