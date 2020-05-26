#0 1 1 2 3 5 8.....

n=int(input("Enter the number for febonacci:"))
if n==1:
  f1=0
  print(f1)

elif n==2:
  f1=0
  f2=1
  print(f1,f2)

else:
  f1=0
  f2=1
  print(f1,f2,end=" ")
for i in range(2,n):
  f3=f1+f2
  f1=f2
  f2=f3
  print(f3,end=" ")

"""
0    1    1    2   3


f1=2
f2=3
f3=3"""
