class Student:
    school = "AkiraChix"
    def __init__(self, firstname, secondname, age, country):
     self.firstname = firstname
     self.secondname = secondname
     self.age = age
     self.country = country
    def greet(self):
         return f"Hello {self.firstname} from {self.country}. Welcome to {self.school}"
    def Full_name(self):
        return f"Hello {self.firstname} {self.secondname}"
    def year_of_birth(self):
        year = 2022 - self.age
        return f"Hello {self.firstname}, you were born in {year}"
    def initials(self):
        return f"Hello your initial is {self.firstname[0]}{self.secondname[0]}"

