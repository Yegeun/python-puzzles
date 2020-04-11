# 2520 is divisible by 1 to 10 2520 should be kept adding to see if all adding is neeeded

num = 2520
num1 = 2520
while True:
  num1 = num ## checks if its the same as before
  for i in range (10,21): ## checks if its divisible by 10 or 21
    if num%i!=0:
      num = num + 2520
      break
  print(num)
  if num==num1:
    break


print(num)