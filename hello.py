class student:
    def __init__(self,name,age,marks,department):
        self.name=name
        self.age=age
        self.marks=marks
        self.department=department

    def call(self):
        print(f"Name {self.name}")
        print(f"Age {self.age}")
        print(f"Marks {self.marks}")
        print(f"Department {self.department}")

    def average_marks(self):
        total=0
        num=len(self.marks)
        for i in self.marks:
            total+=i
        print(f"Average {total/num}")

x=student("Aashir", 21,[10,20,30],"bscs")
x.call()
x.average_marks()

y=student("Yasir", 27,[40,50,60],"mechatronics engineer")
y.call()
y.average_marks()