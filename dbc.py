import mysql.connector

from cat import Cat

class Database:
    # Open connection to SQL server
    def __init__(self):
        self.cnx = mysql.connector.connect(
            user='root',
            password='navydata',
            host='127.0.0.1',
            database='pets'
        )

    # Close connection to SQL server
    def __del__(self):
        self.cnx.close()

    # Select all rows from DB and return as list of Cats
    def listAllCats(self):
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM cats")
        cursor.execute(query)

        cats = []
        for (id, name, owner, birth) in cursor:
            cats.append(Cat(name, owner, birth))
        
        cursor.close()
        return cats

    # Insert new cat into DB
    # Take in Cat object and return the newly created row ID
    def insertCat(self, kitty: Cat):
        cursor = self.cnx.cursor()
        addCatQuery = ("INSERT INTO cats "
               "(name, owner, birth) "
               "VALUES (%s, %s, %s)")
        kittyData = (kitty.name, kitty.owner, str(kitty.birthdate))
        cursor.execute(addCatQuery, kittyData)
        return cursor.lastrowid
