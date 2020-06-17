# our channel is skylight 4u
s=input("Enter the string:")
a=s.split()     #['our', 'channel', 'is', 'skylight']
#print(a)
for i in a:
  l=len(i)
  if l%2==0:
    print(i)