# Largest prime factor
# ------------------------------------------------- #
# Check if number is dividable by fac, if it is divide
# by fac, else increment fac, until fac is not less than
# number.
# ------------------------------------------------- #

num, fac = 600851475143, 2
while fac*fac <= num:
  if num%fac==0:
    num //= fac
  else:
    fac+=1
print "Project Euler #3:"
print "The largest prime factor of the number 600851475143 is", num
