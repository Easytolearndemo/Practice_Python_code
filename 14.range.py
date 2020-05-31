for j in range(3,100):
  c=0
  for i in range(1,j+1):
    if j%i==0:
      c=c+1
  if c==2:
    print(j)
