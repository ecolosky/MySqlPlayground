from datetime import date

class Cat:
    def __init__(self, name: str, owner: str, birthdate: date):
        self.name = name
        self.owner = owner
        self.birthdate = birthdate
    
    def __str__(self):
        return "{}, owned by {} was born on {}".format(self.name, self.owner, self.birthdate)