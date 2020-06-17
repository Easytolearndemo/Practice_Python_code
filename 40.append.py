#append()
#Syntax:array_name.append(new_element)
from array import *
a=array('i',[5,2,3,1,7])
a.append(10)
for i in range(len(a)):
  print(a[i])