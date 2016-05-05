# Multiples of 3 and 5
# ------------------------------------------------- #
# Get the numbers that are dividable with 3 and 5.
# Sum all those numbers together.
# ------------------------------------------------- #

sum=0
for a in range(0, 1000):
  if a%5 is 0 or a%3 is 0:
    sum=sum+a
print "Project Euler #1:"
print "The sum of all multiples of 3 or 5 below 1000 is", sum
