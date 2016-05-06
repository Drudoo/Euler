# Summation of primes
# ------------------------------------------------- #
# Reuse isPrime from Euler_7. While number is less
# than 2000000 check if the number is prime, if it is
# then add it to result.
# ------------------------------------------------- #

num, result=1,0
def isPrime(n):
    if n==1: return False
    elif n<4: return True
    elif n%2==0: return False
    elif n<9: return True
    else:
        d = 3
        while d * d <= n:
            if n%d == 0:
                return False
            d += 2
        return True

while num < 2000000:
    if isPrime(num):
        result+= num
    num+=1

print "Project Euler #10"
print "What is the sum of primes below two million?", result
