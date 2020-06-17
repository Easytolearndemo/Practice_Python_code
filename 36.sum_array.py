# Sum of array 
from array import *
s=0
a=array('i',[])
n=int(input("Enter how many element:"))
for i in range(n):
  a.append(int(input("Enter the element:")))
for i in range(len(a)):
  s=s+a[i]
print(f"Sum of array is:{s}")
