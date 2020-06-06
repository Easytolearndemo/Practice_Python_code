def maxi(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  else:
    return c


x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=int(input("Enter 3rd number:"))
ans=maxi(x,y,z)
print(f"Th highest number is {ans}")