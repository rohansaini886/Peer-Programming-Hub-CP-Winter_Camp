*l, a, b = map(int, input().split())
print(max(0, min(b + 1, *l) - a))
