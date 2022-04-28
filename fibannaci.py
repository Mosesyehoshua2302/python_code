# F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1

# Takes user input and presents coorelating fibonacci number

def fib(n): 
  if n < 0: 
    print(" Wrong input duffus")
  elif n == 0: 
    return 0   
  elif n ==1 or n == 2: 
    return 1
  else: 
    return fib(n-1) + fib(n-2) 


print(fib(9)) 
