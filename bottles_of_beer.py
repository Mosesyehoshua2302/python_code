


def song(num_of_bottles): 
  
  while num_of_bottles >= 2:
    if num_of_bottles > 2:
      print(str(num_of_bottles) + " bottles of beer on the wall" )
      print(str(num_of_bottles) + " bottles of beer" )
      print("take one down, pass it around ")
      print(str(num_of_bottles-1) + " bottles of beers on the wall")
      print( "------ ---------- ---------- ------- ")
      num_of_bottles -= 1

    else:
      print("1" + " bottles of beer on the wall" )
      print("1" + " bottles of beer" )
      print("take one down, pass it around ")
      print("ZERO" + " bottles of beers on the wall")
      print( "------ ---------- ---------- ------- ")

      break


song(45) 

