#Factorial of a number

#5!=5*4*3*2*1=120
n=int(input("Enter a number:"))
f=1
a=0
while a!=n:
  f=f*n
  n=n-1
print(f"Factorial={f}")


"""n=5-1=4-1=3-1=2-1=1-1=0
f=1*5=5*4=20*3=60*2=120*1=120
a=0"""

