import os
import csv
from Objects import CustomError, ImpossibleOutcome, misc, c
import sqlite3 
#imma be honest i couldnt get it to work in sqlite3 
class datawork():
   def get_player_by_name(player_name):
         try:
            with open(SaveGame, mode='r', newline='') as file:
                reader = csv.reader(file)
                data = list(reader)

            for row in data[1:]:
                if row[0].lower() == player_name.lower():
                    return {
                        'name': row[0],
                        'position': row[1],
                        'at_bats': int(row[2]),
                        'hits': int(row[3]),
                        'avg': float(row[4])
                    }

            # Player not found
            return None
         except FileNotFoundError as ex:
            raise CustomError(f"File {SaveGame} not found.", code=404)
         except PermissionError as ex:
            raise CustomError(f"Permission denied for file {SaveGame}.", code=403)
         except Exception as ex:
            raise CustomError(f"An error occurred: {ex}", code=500)
    # i wanted to have alot of features so chat gpt did help with this. i do know whats going on though
   def remove(debug):
       try:
        with open(SaveGame, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        datawork.printresults()  # Print the current data before removal
        
        player_name = input("Enter player's name to remove: ").lower()
        
        found = False
        new_data = []
        
        for row in data:
            if row[0].lower() == player_name:
                found = True
                continue
            new_data.append(row)
        
        if found:
            with open(SaveGame, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)
            
            print(f"{c.GREEN}Player {player_name} removed successfully.{c.ENDC}")
        else:
            print(f"{c.FAIL}Player {player_name} not found.{c.ENDC}")
       except FileNotFoundError as ex:
            misc.exceptionhandle(ex, debug, f"File {SaveGame} not found.")
       except PermissionError as ex:
            misc.exceptionhandle(ex, debug, f"Permission denied for file {SaveGame}.")
       except Exception as ex:
            misc.exceptionhandle(ex, debug)
    

   def printresults():
    misc.printsigns()
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
    misc.printsigns()

   def addmember(debug):
       #chatgpt wrote this i modified it (added exception handling and valid checks)
        new_player_name = input("Enter player's name: ")
        new_player_position = input("Enter player's position: ")
        while True:
         try:
          new_player_ab = int(input("Enter player's at-bats: "))
          if (new_player_ab < 0): raise ValueError("How did we get here")
          break
         except ValueError as ex: misc.exceptionhandle(ex,debug,"Please enter a valid whole number")
         except Exception as ex: misc.exceptionhandle(ex,debug)
        while True:
         try:
          new_player_hits = int(input("Enter player's hits: "))
          if (new_player_ab < new_player_hits or new_player_hits < 0): raise ImpossibleOutcome("How did we get here")
          else:
           break
         except ImpossibleOutcome as ex: misc.exceptionhandle(ex,debug,"Bat must be equal or greater then hit count and must be above zero") 
         except ValueError as ex: misc.exceptionhandle(ex,debug,"Please enter a valid whole number")
         except Exception as ex: misc.exceptionhandle(ex,debug)
        new_player_avg = new_player_hits / new_player_ab if new_player_ab > 0 else 0.0

        new_player_entry = [new_player_name, new_player_position, new_player_ab, new_player_hits, new_player_avg]

        with open(SaveGame, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_player_entry)
   def move_player(debug):
        try:
            with open(SaveGame, mode='r', newline='') as file:
                reader = csv.reader(file)
                data = list(reader)
            
            datawork.printresults()  # Print the current data before moving
            
            player_name = input("Enter player's name to move: ").lower()  # Convert input to lowercase
            
            found = False
            index = None

            for i, row in enumerate(data):
                if row[0].lower() == player_name:  # Convert row name to lowercase for comparison
                    found = True
                    index = i
                    break
            
            if found:
                new_position = input("Enter new position for the player: ")

                data[index][1] = new_position  # Update the position
                
                with open(SaveGame, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                
                print(f"{c.GREEN}Player {player_name} moved successfully to {new_position}.{c.ENDC}")
            else:
                print(f"{c.FAIL}Player {player_name} not found.{c.ENDC}")
        except FileNotFoundError as ex:
            misc.exceptionhandle(ex, debug, f"File {SaveGame} not found.")
        except PermissionError as ex:
            misc.exceptionhandle(ex, debug, f"Permission denied for file {SaveGame}.")
        except Exception as ex:
            misc.exceptionhandle(ex, debug)
   def edit_stats(debug):
        try:
            with open(SaveGame, mode='r', newline='') as file:
                reader = csv.reader(file)
                data = list(reader)
            
            datawork.printresults()  # Print the current data before editing
            
            player_name = input("Enter player's name to edit stats: ").lower()  # Convert input to lowercase
            
            found = False
            index = None

            for i, row in enumerate(data):
                if row[0].lower() == player_name:  # Convert row name to lowercase for comparison
                    found = True
                    index = i
                    break
            
            if found:
                new_ab = int(input(f"Enter new at-bats for {player_name}: "))
                new_hits = int(input(f"Enter new hits for {player_name}: "))
                
                if new_ab < 0 or new_hits < 0 or new_hits > new_ab:
                    raise ImpossibleOutcome("How did we get here")
                
                new_avg = new_hits / new_ab if new_ab > 0 else 0.0

                data[index][2] = new_ab  # Update at-bats
                data[index][3] = new_hits  # Update hits
                data[index][4] = new_avg  # Update average
                
                with open(SaveGame, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                
                print(f"{c.GREEN}Stats for {player_name} updated successfully.{c.ENDC}")
            else:
                print(f"{c.FAIL}Player {player_name} not found.{c.ENDC}")
        except FileNotFoundError as ex:
            misc.exceptionhandle(ex, debug, f"File {SaveGame} not found.")
        except PermissionError as ex:
            misc.exceptionhandle(ex, debug, f"Permission denied for file {SaveGame}.")
        except ValueError as ex:
            misc.exceptionhandle(ex, debug, "Please enter valid whole numbers.")
        except ImpossibleOutcome as ex:
            misc.exceptionhandle(ex, debug, "Bat must be equal or greater then hit count and must be above zero")
        except Exception as ex:
            misc.exceptionhandle(ex, debug)
env = os.getenv('LOCALAPPDATA')
path = f"{env}\\bobthecorn\\Baseball Game\\"
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)
    print("The new directory is created!")

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
        if datacheck == "y":
            with open(SaveGame, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(Defaultdata)
            break
        elif datacheck == 'n':
            with open(SaveGame, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows([["Player", "POS", "AB", "H", "AVG"]])
            break
        else:
            print(f"{c.FAIL}Invalid input{c.ENDC}")
            pass
    print(f"{c.LIGHT_PURPLE}First time setup complete{c.ENDC}")
    print()
