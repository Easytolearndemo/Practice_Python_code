from array import *
a=array('i',[])
n=int(input("Enter how many element:"))
for i in range(0,n):
  a.append(int(input("Enter the element:")))
r=int(input("Enter the numbre roted how many place:"))
while r!=0:
  temp=a[n-1]
  for i in range(n-1,0,-1):
    a[i]=a[i-1]
  a[0]=temp
  r=r-1

for i in range(len(a)):
    print(a[i])