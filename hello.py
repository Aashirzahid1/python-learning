class Car:
    def __init__(self,brand,model,year):
        self.__brand=brand
        self.model=model
        self.year=year


    def update_brand(self,brand):
        self.__brand=brand


    def display_info(self):
        print(f"Your car brand {self.__brand} and model {self.model} manufacturing year {self.year}")
    
    def start_engine(self):
        print("engine started")

car1=Car("Toyota", "corolla", 2022)
car1.__brand="suzuki"
car1.display_info()
car1.start_engine()
 