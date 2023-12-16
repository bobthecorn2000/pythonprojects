import traceback
class CustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

class ImpossibleOutcome(CustomError):
    def __init__(self, message):
        super().__init__(message, code=86753)
        self.extra_info = "You've done the impossible, you broke the system, i have no idea what you did to see this message"





class misc():
 def printsigns(y = 79):
        for x in range(y):
            print("=",end="")
        print()
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

