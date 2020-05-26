#sum of digit
"""123=6
1+2+3=6
1234=10"""

s=0
n=int(input("Enter a number:"))
while n!=0:
  r=n%10
  s=s+r
  n=n//10
print(f"sum of digit:{s}")
"""
s=6
n=0
r=1"""
