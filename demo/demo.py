import random
class Die:
    
    __value:int = 1

    def getValue(self):
        return self.__value
               
    def roll(self):
        self.__value = random.randrange(1, 7)
    print(__value)