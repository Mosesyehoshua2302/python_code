
Conversion_list = [  
{ "Integer": 1000,"roman": "M" },
{ "Integer": 500, "roman": "D" },
{ "Integer": 100, "roman": "C" },
{ "Integer": 50,  "roman": "L" },
{ "Integer": 10,  "roman": "X" },
{ "Integer": 5,   "roman": "V" },
{ "Integer": 1,   "roman": "I" },


]

def int_to_roman(input_num): 
  output = " "
  
  for Dictionary in Conversion_list: 

#This code is to find out how many times our integer goes into out input_num
    copies = input_num // Dictionary["Integer"] 

#for however many copies create the equivalent roman numerals
    for i  in range(copies): 
      output += Dictionary["roman"]

#for whatever is left over
    input_num = input_num % Dictionary["Integer"]

  
  return output

print(int_to_roman(1000))
   
 


     


