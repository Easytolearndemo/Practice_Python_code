#array_name.insert(position_number, new_element)
"""from array import *
a=array('i',[5,2,3,1,7])
a.insert(2,10)
for i in range(len(a)):
  print(a[i])"""


from array import *
a=array('i',[])
n=int(input("Enter how many element:"))
for i in range(n):
  a.append(int(input("Enter the element")))
pos=int(input("Enter the position:"))
item=int(input("Enter the item:"))
a.insert(pos,item)
for i in range(len(a)):
  print(a[i])