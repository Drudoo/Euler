# Highly divisible triangular number
# ------------------------------------------------- #
# Return triangle number, return number of factors.
# While factors less than 500, get the triangle number,
# then the factors of that number. 
# ------------------------------------------------- #

def t(n):
    return (n*(n+1))/2

def tau(n):
    sqrt,t=int(n**0.5),0
    for factor in range(1, sqrt+1):
        if n % factor == 0:
            t+=2
    if sqrt*sqrt==n:
        t -=1
    return t

result,d,num,_tau=0,0,0,0
while _tau < 500:
    _t=t(d)
    _tau=tau(_t)
    if result < _tau:
        result = _tau
        num=d
    d+=1
print "Project Euler #12:"
print "The value of the first triangle number is", t(num)
