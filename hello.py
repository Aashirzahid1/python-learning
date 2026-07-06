class animal:
    def __init__(self, name, sound):
        self.name=name
        self.sound=sound

class dog(animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def detail(self):
        print(f"{self.name} sound {self.sound}")


dog1=dog("smarto","woof")

dog1.detail()