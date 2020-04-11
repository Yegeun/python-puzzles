'''
By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.'''
n = 0  # start
n1 = 1  # start 1
n3= 0 # end number
exceed= 4000000 # ecxeeds four million change this number for the exceed
num_list = [] #list of all the numbers

while (n3<exceed): # it doesn't exceed 4 million
    n3 = n + n1
    if (n3<4000000):
        if (n3%2==0): #checks if its an even number
            num_list.append(n3) #appends it is an even number
        n = n1
        n1 = n3
        #print(n3) check that all numbers afre fibb
print(sum(num_list))

