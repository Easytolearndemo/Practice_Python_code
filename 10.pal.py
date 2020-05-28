n=int(input("Enter the number:"))
p=n
s=0
while n!=0:
  r=n%10
  s=s*10+r
  n=n//10
if s==p:
  print(f"the {p} is palindrome")
else:
  print(f"the {p} is not palindrome")