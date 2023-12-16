import os
import traceback
import csv
from Objects import misc, c
from UI import assets
import sqlite3


debug = "Disable"
position = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P']


print(misc.mid(79) + f"{c.LIGHT_BLUE}Baseball Team Manager{c.ENDC}")
assets.menu(debug, position) 