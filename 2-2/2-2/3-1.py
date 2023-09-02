#!/usr/bin/env python3
 
invalid = 1
goagain = "y"
# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
while goagain == "y" :
   invalid = 1
   while invalid == 1 : 
    try :
        miles_driven = float(input("Enter miles driven:         "))
        if miles_driven <= 0:
            print("Miles driven must be greater than zero. Please try again.")
            pass
        else :
            invalid = 0
        
    except:
        print("please enter a number")
        pass
   invalid = 1
   while invalid == 1 : 
    try :
        gallons_used = float(input("Enter gallons of gas used:  "))

  
        if gallons_used <= 0:
            print("Gallons used must be greater than zero. Please try again.")
            pass
        else :
            invalid = 0
        
    except:
        print("please enter a number")
        pass          
    
   invalid = 1
   while invalid == 1 :
        try :
            gallons_cost = float(input("Enter the cost per gallon:  "))
            if gallons_cost < 0 : 
                print("the cost must be greater then zero. please try again")
                pass
            else :
                invalid = 0

        except:
            print("please enter a number")
            pass          
# calculate and display miles per gallon
   invalid = 1
   mpg = round(miles_driven / gallons_used, 2)
   total = round(gallons_used * gallons_cost,1)
   print("Miles Per Gallon:          ", mpg)
   print(f"Total Gas Cost:             {total}")
   print(f"Cost per mile:              {round(total / miles_driven,1)}")

   print()
   while invalid == 1 :
           goagain = input("go again y/n:     ").lower()
           
           if goagain == "y" or goagain == "n" :
                invalid = 0
           else : 
               print("invalid entry try again")
                

print()
print("Bye!")




