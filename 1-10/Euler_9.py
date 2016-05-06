# Special Pythagorean triplet
# ------------------------------------------------- #
# Run through all numbers from 1 to 500 for a,b,c.
# If a^2+b^2=c^2 check if a+b+c=1000. If it does,
# save a*b*c as result. 
# ------------------------------------------------- #

result=0
i,j,k=1,1,1
a,b,c=0,0,0
while i < 500:
    j=1
    while j < 500:
        k=1
        while k < 500:
            if (i**2)+(j**2)==(k**2):
                if i+j+k==1000:
                    result = i*j*k
                    a,b,c=i,j,k
            k+=1
        j+=1
    i+=1

print "Project Euler #9"
print "What is the product abc?", result, a,b,c
