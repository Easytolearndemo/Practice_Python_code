# array input form user and print the element
from array import *
a=array('i',[])
n=int(input("Enter how many element:"))
for i in range(n):
  a.append(int(input("Enter element:")))
print("the array element are:")
for i in range(len(a)):
  print(a[i])