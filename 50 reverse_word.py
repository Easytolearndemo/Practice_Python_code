s=input("Enter the string:")
#s="my youtub channal is skylight 4u"
l=s.split()
#print(l)          ['my', 'youtub', 'channal', 'is', 'skylight', '4u']
l1=l[::-1]
#print(l1)        ['4u', 'skylight', 'is', 'channal', 'youtub', 'my']
ans=' '.join(l1)
print(ans)