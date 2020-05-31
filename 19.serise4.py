#1/1!+2/2!+3/3!........
s=0
f=1
n=int(input("enter the number"))
for i in range(1,n+1):
  f=f*i
  s=s+(i/f)
print(s)
