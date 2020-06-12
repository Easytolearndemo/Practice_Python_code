#Equilateral ==
#Isosceles 2==
#Scalence !
def trang(a,b,c):
  if a==b==c:
    print("Equilateral")

  elif a==b or b==c or a==c:
    print("Isosceles")
  else:
    print("Scalence")


x=int(input("Enter 1st Side:"))
y=int(input("Enter 2nd Side:"))
z=int(input("Enter 3rd Side:"))
trang(x,y,z)