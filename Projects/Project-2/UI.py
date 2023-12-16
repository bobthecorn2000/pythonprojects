import os
from DB import datawork, SaveGame
from Objects import c, misc


class assets:
   



    def printsigns(y = 79):
        for x in range(y):
            print("=",end="")
        print()




    def printmenu(position):
        assets.printsigns()
        print(f'{c.GREEN}Menu Options{c.ENDC}')
        print('1 - Display lineup')
        print('2 - Add player')
        print(f'3 - Remove player')
        print(f'{c.FAINT}4 - Move player{c.ENDC}') # im not quite sure what this is for
        print(f'5 - Edit player position')
        print(f'6 - Edit player stats')
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
                datawork.remove(debug)
                
            elif (option == 4):
                print(f"{c.LIGHT_GRAY}{c.BLINK}( ._.){c.ENDC}")
                
            elif (option == 5):
                datawork.move_player(debug)
            elif (option == 6):
                datawork.edit_stats(debug)
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
           except Exception as Ex: misc.exceptionhandle(Ex,"Enable","There was an issue deleting your SaveData")
         else: misc.exceptionhandle(Ex,debug,"Invalid Input")
         pass
        except Exception as Ex: misc.exceptionhandle(Ex,debug)
  