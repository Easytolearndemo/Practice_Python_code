#Python program for Simple interest formula:
"""si=ptr/100
    si=simple interest
    p=Amount
    r=rate
    t=time
    
    input:
    p=3000
    r=7
    t=1
    output:
    21.0"""

p=int(input("Enter the amount:"))
r=int(input("Enter the rate:"))
t=int(input("Enter the time:"))
si=(p*t*r)/100
print(f"Simple interest is:{si}")