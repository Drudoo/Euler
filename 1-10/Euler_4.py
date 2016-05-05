# Largest palindrome product
# ------------------------------------------------- #
# Run through all numbers from 999 to 100. Check if
# any of them are the same backwards. If they are
# set p equal to the number.
# ------------------------------------------------- #

p=0
for i in range(999,100,-2):
  for j in range(999,100,-2):
    if (str(i*j) == str(i*j)[::-1]):
      if(i*j > p):p=i*j
      break
print "Project Euler #4"
print "The largest palindrome made from the product of two 3-digit numbers is", p
