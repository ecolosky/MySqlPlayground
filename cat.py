class Cat:
    def __init__(self, name, owner, birthdate):
        self.name = name
        self.owner = owner
        self.birthdate = birthdate
    
    def __str__(self):
        return "{}, owned by {} was born on {}".format(self.name, self.owner, self.birthdate)