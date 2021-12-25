n = int(input())
input()
print(min(sum(5 * y + 15 for y in x) for x in (map(int, input().split()) for _ in range(n))))
