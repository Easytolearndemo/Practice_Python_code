n=int(input("Enter the number"))
q=n
p=n
c=0
s=0
while n!=0:
  n=n//10
  c=c+1

while p!=0:
  r=p%10
  s=s+(r**c)
  p=p//10

if s==q:
  print("the number is amstrong")
else:
  print("the number is not amstrong")

"""
n=0
q=153
p=0
c=3
s=153
r=1"""