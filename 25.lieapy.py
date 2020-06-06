y=int(input("Enter the year"))
if y%4==0 and y%100!=0 or y%400==0:
  print(f"The year {y} is leapyear")
else:
  print(f"The year {y} is not leapyear")
