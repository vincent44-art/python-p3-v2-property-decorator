APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff', age=1):
        self.name = name
        self.breed = breed
        self.age = age

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        """The breed property"""
        return self._breed

    @breed.setter
    def breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")

    @property
    def age(self):
        """The age property"""
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and 0 <= age <= 20:
            self._age = age
        else:
            raise ValueError("Age must be an integer between 0 and 20.")
