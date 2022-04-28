def factorial(num): 
  result = 1 #place holder for output
  for n in range(num, 1, -1): # from whatever number minus 1 until you get to 1 but doesnt include 1
    result = result * n
  return result

print(factorial(4)) 

  