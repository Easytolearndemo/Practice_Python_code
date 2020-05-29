n=int(input("enter the number"))
f1=0
f2=1
f3=f1+f2
if n==0 or n==1:
  print("Yes")
else:
  while f3<n:
    f1=f2
    f2=f3
    f3=f1+f2
  if f3==n:
    print("yes")
  else:
    print("No")

"""n=4
f1=2
f2=3
f3=5"""
