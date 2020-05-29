n=int(input("Enter the number:"))
for i in range(2,n):
  q=n%i
  if q==0:
    print(f"the number {n} is not prime")
    break
  else:
    print(f"the number {n} is prime")
    break