# python program for sum of squares of first n natural numbers

s=0
n=int(input("enter the number"))
for i in range(1,n+1):
  s=s+(i**2)
print(s)