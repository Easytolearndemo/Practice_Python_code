c=0
n=int(input("Enter the number"))
for i in range(1,n+1):
  if n%i==0:
    c=c+1
if c==2:
  print(f"prime {n}")
else:
  print(f"not prime {n}")
