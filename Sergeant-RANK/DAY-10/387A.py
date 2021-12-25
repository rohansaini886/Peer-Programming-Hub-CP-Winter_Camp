h1,m1= (map(int,input().split(':')))
m1+=h1*60
h2,m2= (map(int,input().split(':')))
m2+=h2*60
m2=m1-m2
m2%=1440
print("%02d:%02d"%(m2//60,m2%60))
