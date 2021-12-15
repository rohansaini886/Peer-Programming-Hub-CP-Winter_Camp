import calendar
s=input()
n=int(input())
arr=[]
for i in range(1,13):
    a=calendar.month_name[i]
    arr.append(a)
#print(arr)
print(arr[(arr.index(s)+n)%12])
