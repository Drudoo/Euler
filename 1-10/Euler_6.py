# Sum square difference
# ------------------------------------------------- #
# First square all the numbers from 1 to 100. Then
# sum all the numbers and square them. Then
# substract the two results from each other. 
# ------------------------------------------------- #

squared, result, sum = 0,0,0
for i in range(1,101):
  squared+=(i*i)
  sum+=i
result = (sum*sum)-squared
print "Project Euler #6"
print "The difference between the sum of the squares and the square of the sum is", result
