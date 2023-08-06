class PackageB:
    def __init__(self, age: int):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age