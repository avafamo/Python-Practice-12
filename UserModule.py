class Person:
    classAttribute = "test value"

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def showFullName(self):
        return f"{self.name} {self.family}"

    @classmethod
    def showClassAttribute(cls):
        return Person.classAttribute




class User(Person):
    pass


Ava = Person('Ava', 'ordookhani', 25)
sara = User('sara', 'moradi', 24)

# print(Ava.name)
#
# print(sara.showFullName())
#
# print(User.classAttribute)

# print(User.showClassAttribute())

print(sara.name)