a,b=input(),input()
print(("NO","YES")[str(int(a)+int(b)).replace("0","")==str(int(a.replace("0",""))+int(b.replace("0","")))])
