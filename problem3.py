'''Find the largest palindrome made from the product of two 3-digit
numbers. '''

numlist = []


# want the largest just go the other way to find the largest

def checkPalindrome(word): ##checks if its palindrome
  word = str(word)
  word = list(word)
  length=len(word)
  half = length//2
  for k in range(half):
    if word[k] != word[length-k-1]:
      return False
  return True

for i in range(100, 1000):  # thankfully timesing commutative
  for j in range(100, 1000):  # goes throught every number and times all 3 digit numbers
    x2 = i * j
    if checkPalindrome(x2) == True: # if its true it will append it to a list
      numlist.append(x2)
print(max(numlist))
