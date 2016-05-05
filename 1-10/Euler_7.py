# 10001st prime
# ------------------------------------------------- #
# 1 or even number is not prime. 2,3,5,7 is prime.
# Else check if n mod d where d is uneven number.
# Run it until 10001 primes are found. 
# ------------------------------------------------- #

num, result, count=1,0,0
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

while count < 10001:
    if isPrime(num):
        result = num
        count+=1
    num+=1

print "Project Euler #7"
print "What is the 10 001st prime number?", result
