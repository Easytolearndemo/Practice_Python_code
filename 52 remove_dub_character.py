s=input("Enter a string:")
i=0
s1=""
for x in s:
  l=s.index(x)
  # print(x,l)
  if l==i:
    s1=s1+x
  i=i+1
print(s1)