class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        
    def eat(self):
        self.is_hungry = False

    def walk(self):
        print(f"{self.name} is walking.")

class Pets:

    tom = Dog("Tom", 6)
    fletcher = Dog("Fletcher", 7)
    larry = Dog("Larry", 9)
    tom.eat()
    fletcher.eat()
    larry.eat()

pets = Pets()

info = f"""
    I have 3 dogs.
    {pets.tom.name} is {pets.tom.age}
    {pets.fletcher.name} is {pets.fletcher.age}
    {pets.larry.name} is {pets.larry.age}
    {pets.tom.walk()}
    {pets.fletcher.walk()}
    {pets.larry.walk()}
    
    And they're all mammals, of course
"""
print(info)
status = pets.tom.is_hungry == True and pets.fletcher.is_hungry == False and pets.larry.is_hungry == False

if status:
    print("My dogs are not hungry!")
