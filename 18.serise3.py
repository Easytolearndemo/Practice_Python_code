#1/1+1/2+1/3+1/4.....

s=0
n=int(input("enter the number"))
for i in range(1,n+1):
  s=s+(1/i)
print(s)
