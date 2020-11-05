from datetime import date

from cat import Cat
from dbc import Database

# Creating a database object will open a connection with the mysql server and allow further db operations
database = Database()

# How to insert a new object into the database
# fitz = Cat('Fitzgerald', 'Caroline', date(2016, 4, 1))
# newId = database.insertCat(fitz)
# print(newId)

# How to select data out of the database
for cat in database.listAllCats():
    print(cat)

# At the end of the program the database object must be deleted to close the connection to the mysql server
del database
