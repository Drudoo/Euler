# Multiples of 3 and 5
# ------------------------------------------------- #
# Check all Fibonacci numbers less than 4 million.
# If they are even, then sum them
# ------------------------------------------------- #

a,b,sum=1,1,0
while a < 4*10**6:
  if a %2 == 0:
    sum+=a
  a,b=b,a+b
print "Project Euler #2:"
print "The sum of the even-valued terms not exceeding four million is", sum
