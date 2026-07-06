class animal:
    def __init__(self, name, sound):
        self.__name=name
        self.sound=sound

    def detail(self):
        print(f"{self.__name} sound {self.sound}")

class dog(animal):
    def __init__(self, age, name, sound):
        super().__init__(name,sound)
        self.age=age
        self.gender="Male"

   


dog1=dog(55,"smarto","woof")

dog1.detail()