line = "100 1000"
line = line.split()
low = (int(line[0]))
high = (int(line[1]))

random = []

for i in range(low, high):
  temp = str(i)
  temp1 = list(temp)
  for elem in temp:
    if temp.count(elem) > 1:
      print("this has dup")
    else:
      random.append(temp1)
print(random)
