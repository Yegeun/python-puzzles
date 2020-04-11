# strips the row
import csv

# min max solver start from the bottom and take it to the top?
temploop = []
tempdata = []
for i in range(100):
  temploop.append(0)
  tempdata.append(0)

linenumbers = []

with open("triangle.txt") as file:
  reader = csv.reader(file)  # change contents to floats
  for row in reader:  # each row is a list
    linenumbers.append(row)


def changelist(data):
  row_data = max(data)  # converts it into 1d list you
  row_data = row_data.split(" ")
  row_data = [int(i) for i in row_data]
  return row_data


# loop
for i in range(99, -1, -1):
  # intialise the first row of row
  temp = changelist(linenumbers[i])
  # splits into each row
  if i == 0:
    tempdata[j] = temp[j]
  for j in range(i):  # finds out the max between the numbers
    tempdata[j] = max(temp[j], temp[j + 1])
  for k in range(0, i+1):
    temploop[k] = (temploop[k] + tempdata[k])
  if i ==0:
    print(temploop[0])
    break
  print(temploop[0:i])
