
import os
import traceback
import csv

class CustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
class ImpossibleOutcome(CustomError):
    def __init__(self, message):
        super().__init__(message, code=86753)
        self.extra_info = "You've done the impossible, you broke the system, i have no idea what you did to see this message"
    

class c:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    #extra ansi colors from github
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"

class assets:
    
    def mid(x):
       
       x = x / 3
       x = int(x)
       y = " " * x
       return y

    def exceptionhandle(Ex, debug: str = "Disable", errormessage: str = "I just don't know what went wrong"):
        if (debug == 'Enable'):
            print(f"{c.FAIL} {errormessage} \n")
            print(f"{Ex}")
            if hasattr(Ex, 'code'):
             print(f"Error code: {Ex.code}")
            if hasattr(Ex, 'extra_info'):
             print(f"additional note: {Ex.extra_info}")
            print("\n {\n")
            traceback.print_tb(Ex.__traceback__)
            print("\n }")
            c.ENDC
        else:print(f"{c.FAIL} {errormessage}")
        print(f'{c.ENDC}',end="")    



    def printsigns(y = 79):
        for x in range(y):
            print("=",end="")
        print()




    def printmenu(position):
        assets.printsigns()
        print(f'{c.GREEN}Menu Options{c.ENDC}')
        print('1 - Display lineup')
        print('2 - Add player')
        print(f'{c.FAINT}3 - Remove player')
        print('4 - Move player')
        print('5 - Edit player position')
        print(f'6 - Edit player stats{c.ENDC}')
        print('7 - Exit program')
        print(f'8 - enable/disable debug')
        print()
        print('POSITIONS')
        for x in position[:-1]:
         print(x+", ",end="")
        print(position[-1])
        assets.printsigns()
        


    def menu(debug,position):
     while True:
        print(f'{c.ENDC}',end="")
        assets.printmenu(position);
     
        
        RawOption = input(":")
        try:
            option = int(RawOption)
            if (option == 1):
                print(f"{c.GREEN}Displaying Lineup{c.ENDC}")
                datawork.printresults()

                
            elif (option == 2):
                print(f"{c.GREEN}Adding Another Player{c.ENDC}")
                datawork.addmember(debug)
            elif (option == 3):
                print(f"{c.LIGHT_GRAY}{c.BLINK}( ._.) no work yet{c.ENDC}")
            elif (option == 4):
                print(f"{c.LIGHT_GRAY}{c.BLINK}( ._.) no work yet{c.ENDC}")
            elif (option == 5):
                print(f"{c.LIGHT_GRAY}{c.BLINK}( ._.) no work yet{c.ENDC}")
            elif (option == 6):
                print(f"{c.LIGHT_GRAY}{c.BLINK}( ._.) no work yet{c.ENDC}")
            elif (option == 7):
                return
            elif (option == 8):
                if (debug == "Enable"):
                    debug = 'Disable'
                    print(f"{c.GREEN}debug is disabled{c.ENDC}")
                else: 
                 debug = 'Enable' 
                 print(f"{c.WARNING}debug is enabled{c.ENDC}")
                 
            else:
                print(f"{c.FAIL}Invalid Input")
        except ValueError as Ex:
        
         if (RawOption == "deletemysavedata"):
           try:
            os.remove(SaveGame)
            print(f"{c.GREEN}SaveGame deleted successfully.{c.ENDC}")
            return
           except Exception as Ex: assets.exceptionhandle(Ex,"Enable","There was an issue deleting your SaveData")
         else: assets.exceptionhandle(Ex,debug,"Invalid Input")
         pass
        except Exception as Ex: assets.exceptionhandle(Ex,debug)
       # if (option == 1):

class datawork():
   
   def printresults():
    assets.printsigns()
    with open(SaveGame, mode='r') as file:
                    reader = csv.reader(file)
                    data = list(reader)
    def print_row(row):
        print("{:<20} {:<5} {:<5} {:<5} {:<5}".format(*row))
        
# Print the header row
    print_row(data[0])
    print("-" * 79)  # Print a dashed line for separation

# Print the rest of the data
    for row in data[1:]:
        print_row(row)
    assets.printsigns()

   def addmember(debug):
       #chatgpt wrote this i modified it (added exception handling and valid checks)
        new_player_name = input("Enter player's name: ")
        new_player_position = input("Enter player's position: ")
        while True:
         try:
          new_player_ab = int(input("Enter player's at-bats: "))
          if (new_player_ab < 0): raise ValueError("How did we get here")
          break
         except ValueError as ex: assets.exceptionhandle(ex,debug,"Please enter a valid whole number")
         except Exception as ex: assets.exceptionhandle(ex,debug)
        while True:
         try:
          new_player_hits = int(input("Enter player's hits: "))
          if (new_player_ab < new_player_hits or new_player_hits < 0): raise ImpossibleOutcome("How did we get here")
          else:
           break
         except ImpossibleOutcome as ex: assets.exceptionhandle(ex,debug,"Bat must be equal or greater then hit count and must be above zero") 
         except ValueError as ex: assets.exceptionhandle(ex,debug,"Please enter a valid whole number")
         except Exception as ex: assets.exceptionhandle(ex,debug)
        new_player_avg = new_player_hits / new_player_ab if new_player_ab > 0 else 0.0

        new_player_entry = [new_player_name, new_player_position, new_player_ab, new_player_hits, new_player_avg]

        with open(SaveGame, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_player_entry)


debug = "Disable"
position = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P']
env = os.getenv('LOCALAPPDATA')
path = f"{env}\\bobthecorn\\Baseball Game\\"
isExist = os.path.exists(path)
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory is created!")

# a file in the current directory
SaveGame = path + "SaveGame.gcsd"
Defaultdata = [
    ["Player", "POS", "AB", "H", "AVG"],
    ["Gordon Freeman", "3B", 1316, 360, 0.274],
    ["Alyx Vance", "RF", 563, 168, 0.298],
    ["Barney Calhoun", "2B", 1473, 407, 0.276],
    ["Eli Vance", "C", 4575, 1380, 0.302],
    ["Isaac Kleiner", "1B", 3811, 1003, 0.263],
    ["Judith Mossman", "SS", 4402, 1099, 0.25],
    ["Dog", "LF", 586, 160, 0.273],
    ["Wallace Breen", "CF", 569, 147, 0.258],
    ["The G-Man", "P", 56, 2, 0.036]
]
isExist = os.path.isfile(SaveGame) 
if not isExist:
  while True:
   datacheck = input(f"{c.LIGHT_PURPLE}First time setup. Use default data? y/n:{c.ENDC}").lower()
   if (datacheck == "y"):
    with open(SaveGame, mode='w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(Defaultdata)
    break
   elif (datacheck == 'n'):
     with open(SaveGame, mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows([["Player", "POS", "AB", "H", "AVG"]])
     break
   else: 
       print(f"{c.FAIL}Invalid input{c.ENDC}")
       pass
  print(f"{c.LIGHT_PURPLE}First time setup complete{c.ENDC}")
  print()
   



print(assets.mid(79) + f"{c.LIGHT_BLUE}Baseball Team Manager{c.ENDC}")      
assets.menu(debug, position)

