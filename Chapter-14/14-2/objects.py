
from dataclasses import dataclass


@dataclass 
class Movie: 

    name:str = ""
    year:int = 1901
    def getstr(self):
        return f"{self.name} ({self.year})"
     

    
