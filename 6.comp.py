"""ci=p(1+r/100)t
p=amount
r=rate
t=time

output:
p=1200
r=5.4
t=2
1333"""

p=int(input("Enter the amount"))
r=float(input("Enter the rate"))
t=int(input("Enter the time"))

ci=(p*(1+r/100)**t)
print(f"CI={ci}")

