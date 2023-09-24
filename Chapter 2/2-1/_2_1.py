
#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
gallons_cost = float(input("Enter the cost per gallon:\t"))
total = round(gallons_used * gallons_cost,1)
# calculate miles per gallon
1

mpg = round(miles_driven / gallons_used, 1)
            
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Total Gas Cost:\t\t{total}")
print(f"Cost per mile:\t\t{round(total / miles_driven,1)}")
print()
print("Bye!")


