#!/usr/bin/env python3
import csv
import os
env = os.getenv('LOCALAPPDATA')
path = f"{env}\\bobthecorn\\7-1\\"
isExist = os.path.exists(path)
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory is created!")
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    #print(os.environ)
    print()
    with open(path + "\\trips.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["miles driven", "gallons used", "calculated value"]
        writer.writerow(field)

        more = "y"
        while more.lower() == "y":
            miles_driven = get_miles_driven()
            gallons_used = get_gallons_used()
                                 
            mpg = round((miles_driven / gallons_used), 2)
            print(f"Miles Per Gallon:\t{mpg}")
            print()
            writer.writerow([miles_driven, gallons_used, mpg])
            more = input("More entries? (y or n): ")
    
    print("Bye!")

if __name__ == "__main__":
    main()

