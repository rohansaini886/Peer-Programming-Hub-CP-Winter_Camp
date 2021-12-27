import math
a=int(input())
x=0
for i in range(2,a):
 z=a
 while z>=1:
 	x+=z%i
 	#print(z%i)
 	z=z//i
 
y=a-2 	
d=math.gcd(x,y)
print(str(x//d)+'/'+str(y//d))
 	
