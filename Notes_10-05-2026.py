class Employees:
    def __init__(self, name, age, team, department):
        self.name = name
        self.age = age
        self.team = team        
        self.department = department
        self.salary = 1000

    def talk_about_yourself(self):
        print(f"My name is {self.name}, I am {self.age} years old, and I work in the {self.team} team of the {self.department} department.")

emp = Employees("Leena", 30, "Data Science", "Analytics")
print(emp.name)
print(emp.age)
emp.talk_about_yourself()


###################
# create another class called dog
