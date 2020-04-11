n = 110001  # change this number
i = 2  # start of the prime number
import math
num = 8
numlist= []
while True:
  for i in range(2,int(math.sqrt(num))):
    if num % i == 0:
      break # breaks out of the for loops if it divisilbe
  else:
    numlist.append(num)
  if len(numlist)==10001:
    break
  num = num + 1
print(numlist[10000])