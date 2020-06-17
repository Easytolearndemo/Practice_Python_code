#array_name.extend(arr)
from array import *
array1=array('i',[7,2,3,9,8])
array2=array('i',[8,9,2,1,3])
array2.extend(array1)
for i in range(len(array2)):
  print(array2[i])
