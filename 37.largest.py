# Largest element in ana array
from array import *
a=array('i',[])
n=int(input("Enter how many element:"))
for i in  range(n):
  a.append(int(input("Enter the element:")))
big=a[0]
for i in range(1,len(a)):
  if a[i]>big:
    big=a[i]
print(f"The largest element is:{big}")