
#!/usr/bin/env python3
import traceback 
import valid
class colors:
 WARNING = '\033[93m'
 FAIL = '\033[91m'
 ENDC = '\033[0m'
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value


#def get_float(prompt,low,high):
#    #imma be honest there are like 10 better ways to do this. but this is kinda what came out
#   invalid = 1
#   while invalid >= 1 :
#    try :
#        if invalid == 1 :
#        #ok i looked at the way the book handles the prompt. i guess i didnt really know what it was asking for. regardless this may be funky but it does work
#         result = float(prompt)
#        if invalid == 2 :
#          result = float(input(f"{colors.WARNING}your answer must be greater then {low} and less then {high}:{colors.ENDC}"))

        
#        if result > low and result <= high :
#          invalid = 0
#          return(result)
#        else: invalid = 2 
            
            
        
#    except Exception as exc:
#        print(f"{colors.FAIL}I just don't know what went wrong \n")
#        print(exc)
#        print("\n {\n")
#        traceback.print_tb(exc.__traceback__)
#        print("\n }")
#        colors.ENDC
#        invalid = 2
#        pass
#def get_int(prompt,low,high) :
#   invalid = 1
#   while invalid >= 1 :
#    try :
#        if invalid == 1 :
       
#         result = int(prompt)
#        if invalid == 2 :
#          result = int(input(f"{colors.WARNING}your answer must be greater then {low} and less then {high}:{colors.ENDC}"))

        
#        if result > low and result <= high :
#          invalid = 0
#          return(result)
#        else: invalid = 2 
            
            
        
#    except Exception as exc:
#        print(f"{colors.FAIL}I just don't know what went wrong \n")
#        print(exc)
#        print("\n {\n")
#        traceback.print_tb(exc.__traceback__)
#        print("\n }")
#        colors.ENDC
#        invalid = 2
#        pass

def main():
    
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = valid.get_float(input("Enter monthly investment:\t"),0,1000)
        yearly_interest_rate = valid.get_float(input("Enter yearly interest rate:\t"),0,15)
        years = valid.get_int(input("Enter number of years:\t\t"),0,50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        check = 1
        while check == 1 :
            choice = input("Continue? (y/n): ").lower()
            if choice == "y" or choice == "n" :
                check = 0
            else: print("invalid option")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
