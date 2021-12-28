n, k = map(int, input().split(" "))

primes = []
n += 1
for x in range(2, n):
	if all((x % p != 0 for p in primes)):
		primes += [x]

for x in range(len(primes) - 1):
   if primes[x] + primes[x+1] + 1 in primes:
      k -= 1

if k <= 0:
	print("YES")
else:
	print("NO")
