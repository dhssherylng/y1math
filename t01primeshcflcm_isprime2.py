# Is num a prime number? 
# A prime number is an integer with exactly 2 different factors, 1 and itself.
# Can you rectify the following program error?

num = 61
num_factors = 0
for i in range(1,num+1): 
  if num % i == 0:
    num_factors += 1
    prime = False
if num_factors == 2
    prime = True
  
print(prime)
