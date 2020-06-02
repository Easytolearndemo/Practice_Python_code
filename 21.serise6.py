#1!+2!+3!+4!+5!.....+n!
s=0
f=1
n=int(input("enter the number"))
for i in range(1,n+1):
  f=f*i
  s=s+f
print(s)