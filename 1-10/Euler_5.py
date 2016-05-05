# Smallest multiple
# ------------------------------------------------- #
# Create function for greatest and lowest common
# denominator. Reduce the range from 1 to 21 (21 excluded)
# using lcd. 
# ------------------------------------------------- #

def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a
def lcd(a,b):
  return a // gcd(a,b)*b
print "Project Euler #5"
print "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is", reduce(lcd,xrange(1,21))
