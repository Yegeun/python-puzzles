'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we

get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

'''

x = 1002 # start value

a = int(x/3) #floors down divisble by 3
b = int(x/5)


num_list = [] #list of all the numbers
while True:
    for i in range(a):
        three = 3 * i #times all the natrual numbes by 3 to get all the number
        num_list.append(three) #appends to the list of number divisble
    for i in range(b):
        three = 5 * i #times all the natrual numbes by 5 to get all the number
        num_list.append(three) #appends to the list of numbers divisble
    break

print(sum(num_list))

