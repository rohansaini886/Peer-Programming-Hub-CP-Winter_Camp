from itertools import accumulate, islice
n = int(input())
a = list(map(int, input().split()))
S = sum(a)
print(sum(S == 2*x for x in islice(accumulate(a), n-1)))
