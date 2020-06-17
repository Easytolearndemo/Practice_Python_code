a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
for i in range(1,a+1):
  if a%i==0 and b%i==0:
    gcd=i
lcm=a*b//gcd
print(f"LCM is:{lcm}")