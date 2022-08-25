class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    

    def speak(self, sound):
        return f"{self.name} barks: {sound}"



class JackRussellTerrier(Dog):
    
    def speak(self, sound="Arf"):
            return super().speak(sound)



buddy = Dog("Buddy", 9)
miles = JackRussellTerrier("Miles", 4)

print(miles.speak())