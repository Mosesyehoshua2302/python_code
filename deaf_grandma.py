
from ast import Break, IsNot


input = input(" Ask Grandma something: ")
lower_case = input.islower()
upper_case = input.isupper()

def response(input): 
  while input != "GOODBYE!":  
    if lower_case:
      print("SPEAK UP, KID!")

    elif upper_case:
      print("NO, NOT SINCE 1946!")
    
    else:
      print("WHAT?!")
    
    break
    
  while input == "GOODBYE!":
      print("LEAVING SO SOON?!")
      break
    
  
  

  

response(input)




#a_string = "hello world"
#all_lowercase = a_string.islower()

#print(all_lowercase)