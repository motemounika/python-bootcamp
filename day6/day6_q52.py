class Animal:
    def speak():
        return"Animal is speaking"
    #single inheritence
class Dog(Animal):
    def Bark():
        return"bow...."
class Puppy(Dog):
    def Puppy():
        return   "Puppy" 
obj1=Animal
obj2=Dog
obj3=Puppy
print(obj1.speak())
print(obj2.Bark())
print(obj3.Puppy)