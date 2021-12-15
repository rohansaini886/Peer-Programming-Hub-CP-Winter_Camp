n = int(input())
l = list(map(int, input().split(" ")))
k = [l.count(1), l.count(2), l.count(3)]
print(n - max(k))
