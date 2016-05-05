# Largest palindrome product
# ------------------------------------------------- #
# Check if number is dividable by fac, if it is divide
# by fac, else increment fac, until fac is not less than
# number.
# ------------------------------------------------- #

p=0
for i in range(999,100,-2):
  for j in range(999,100,-2):
    if (str(i*j) == str(i*j)[::-1]):
      if(i*j > p):p=i*j
      break
print "Project Euler #4"
print "The largest palindrome made from the product of two 3-digit numbers is", p
