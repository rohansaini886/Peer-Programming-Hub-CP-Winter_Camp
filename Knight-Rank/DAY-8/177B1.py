n = int(input())
ans = n
while n != 1:
    i = 2
    while n % i != 0:
        i += 1
    n //= i
    ans += n
print(ans)
