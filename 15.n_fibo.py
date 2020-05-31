n=int(input("Enter the number for febonacci:"))
if n==1:
  f1=0
  print(f1)

elif n==2:
  f2=1
  print(f2)

else:
  f1=0
  f2=1
for i in range(2,n):
  f3=f1+f2
  f1=f2
  f2=f3
print(f3)