def fac(n):
  f=1
  i=1
  if n==0 or n==1:
    return 1

  else:
    while i!=n:
      f=f*n
      n=n-1
    return f


n=int(input("Enetr a number"))
ans=fac(n)
print(f"factorial={ans}")
"""
n=5-1=4-1=3-1=2-1=1
f=1*5=5*4=20*3=60*2=120
i=1"""