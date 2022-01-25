l, r = 1, int(input())

while l < r:
    print(l, r, end=" ")
    l += 1
    r -= 1

if l == r:
    print(l)
