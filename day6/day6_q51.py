class Animal:
    def speak():
        return"Animal is speaking"
    #single inheritence
class Dog(Animal):
    def Bark():
        return"bow...."
obj1=Animal
obj2=Dog
print(obj1.speak())
print(obj2.Bark())