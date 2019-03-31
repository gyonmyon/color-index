while True:
   print("Options:")                                                          
   print("Enter 'ci' to count color index")                                   
   print("Enter 'quit' or 'exit' to end the program")                         
   user_input = input(": ")

   if user_input == "quit":                        #end of the program
      break
   elif user_input == "exit":                      #end of the program
      break
   elif user_input == "ci":                        
      num1 = float(input("Enter a HB: "))
      num2 = float(input("Enter RBC: "))
      result = str( (3 * num1) / (100 * num2) )    #count color index
      print("The answer is " + result)
   
   else:
      print("Unknown input")